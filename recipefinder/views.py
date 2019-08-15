from django.shortcuts import render
import requests
import spoonacular as sp
from recipefinder.models import Recipe, Cart, Ingredient

# apiKey = "bdc5899f1be24e0c9e8dab87a2d3a4f8"
apiKey = "18def195df144c25b76272c62f2b8eab"
maxResults = 3
Cuisines = ["African", "American", "British", "Cajun","Caribbean", "Chinese",
        "Eastern European", "European", "French", "German", "Greek", "Indian",
        "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American",
        "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern",
        "Spanish", "Thai", "Vietnamese"]


# Create your views here.
def home(request):
    thisCart = Cart.objects.get(pk=3)
    thisCart.save()
    return render(request, 'home.html', context={"cartid": thisCart.pk})

def search_recipes(request):
    cartId = request.GET.get('cartid')    
    if request.method == 'GET':
        q = request.GET.get('query')
        c = request.GET.get('cuisineselected')
        if c == "None":        
            url = f'https://api.spoonacular.com/recipes/search?apiKey={apiKey}&query={q}&number={maxResults}'
        else:
            url = f'https://api.spoonacular.com/recipes/search?apiKey={apiKey}&query={q}&cuisine={c}&number={maxResults}'
        response = requests.get(url).json()["results"]
        context={"cuisines": Cuisines, "query": q, "cuisineselected": c, "response": response, "cartid": cartId}
    else:
        context={"cuisines": Cuisines}

    return render(request, 'search_recipes.html', context )

def update_cart(request):
    title = request.GET.get('title')
    recipeid = request.GET.get('id')
    cartId = request.GET.get('cartid')
    thisCart = Cart.objects.get(pk=cartId)

    url = f'https://api.spoonacular.com/recipes/{recipeid}/information?apiKey={apiKey}&includeNutrition=false'
    response = requests.get(url).json()
    recipe = Recipe(recipe_name=response["title"], recipe_id=response["id"], servings=response["servings"], time_required=response["readyInMinutes"], rating=response["spoonacularScore"])
    recipe.save()
    for result in response["extendedIngredients"]:
        ingredient = Ingredient(ingredient_id=result["id"], amount=result["measures"]["us"]["amount"], unit=result["measures"]["us"]["unitLong"], name=result["name"])
        ingredient.save()
        recipe.ingredients.add(ingredient)

    thisCart.recipes.add(recipe)

    return render(request, 'update_cart.html', context={"title": title, "id": recipeid, "recipes": thisCart.recipes.all(), "cartid": cartId})

def remove_from_cart(request):
    cartId = request.GET.get('cartid')
    recipeID = request.GET.get('recipeid')
    thisCart = Cart.objects.get(pk=cartId)
    recipe = Recipe.objects.get(pk=recipeID)
    thisCart.recipes.remove(recipe)
    return render(request, 'update_cart.html', context={"recipes": thisCart.recipes.all(), "cartid": cartId})

def create_list(request):
    cartId = request.GET.get('cartid')
    thisCart = Cart.objects.get(pk=cartId)
    thisCart.ingredients.clear()

    recipes = thisCart.recipes.all()
    for recipe in recipes:
        for ingredient in recipe.ingredients.all():
            if ingredient in thisCart.ingredients.all():
                # for listedIngredient in thisCart.ingredients.all():
                print("this ingredient here:")
                print(ingredient)
                for listedIngredient in thisCart.ingredients.all():
                    if ingredient == listedIngredient:
                        print(ingredient)
                        print(listedIngredient)
                        listedIngredient.amount = listedIngredient.amount + ingredient.amount
                        print(listedIngredient.amount)
                        listedIngredient.save()
            else:
                print("ingredient added")
                thisCart.ingredients.add(ingredient)
                # for listedIngredient in thisCart.ingredients.all():
                #     if ingredient == listedIngredient:
                #         print(listedIngredient.amount)
                #         listedIngredient.amount = listedIngredient.amount + ingredient.amount
                #     else:
                #         thisCart.ingredients.add(ingredient)
    print("Current Cart")
    for ingredient in thisCart.ingredients.all():
        print(ingredient.name)
        print(ingredient)
        print(ingredient.amount)
            
    return render(request, 'create_list.html', context={"recipes": thisCart.recipes.all(), "total_ingredients": thisCart.ingredients.all()})