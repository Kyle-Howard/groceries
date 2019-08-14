from django.shortcuts import render
import requests
import spoonacular as sp
from recipefinder.models import Recipe, Cart

apiKey = "bdc5899f1be24e0c9e8dab87a2d3a4f8"
maxResults = 3
Cuisines = ["African", "American", "British", "Cajun","Caribbean", "Chinese",
        "Eastern European", "European", "French", "German", "Greek", "Indian",
        "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American",
        "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern",
        "Spanish", "Thai", "Vietnamese"]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def search_recipes(request):
    thisCart = Cart.objects.get(pk=3)
    thisCart.save()
    cartId = thisCart.pk

    if request.method == 'GET':
        q = request.GET.get('query')
        c = request.GET.get('cuisineselected')
        if c == "None":        
            url = f'https://api.spoonacular.com/recipes/search?apiKey={apiKey}&query={q}&number={maxResults}'
        else:
            url = f'https://api.spoonacular.com/recipes/search?apiKey={apiKey}&query={q}&cuisine={c}&number={maxResults}'
        response = requests.get(url).json()["results"]
        print(response)
        context={"cuisines": Cuisines, "query": q, "cuisineselected": c, "url": url, "response": response, "cartid": cartId}
    else:
        context={"cuisines": Cuisines}

    return render(request, 'search_recipes.html', context )

def update_cart(request):
    title = request.GET.get('title')
    recipeid = request.GET.get('id')
    cartId = request.GET.get('cartid')
    thisCart = Cart.objects.get(pk=cartId)
    recipe = Recipe(recipe_name=title, recipe_id=recipeid)
    recipe.save()
    thisCart.recipes.add(recipe)

    return render(request, 'update_cart.html', context={"title": title, "id": recipeid, "recipes": thisCart.recipes.all(), "cartid": cartId})

def remove_from_cart(request):
    title = request.GET.get('title')
    recipeid = request.GET.get('id')
    cartId = request.GET.get('cartid')
    recipeID = request.GET.get('recipeid')
    thisCart = Cart.objects.get(pk=cartId)
    recipe = Recipe.objects.get(pk=recipeID)
    thisCart.recipes.remove(recipe)
    return render(request, 'update_cart.html', context={"title": title, "id": recipeid, "recipes": thisCart.recipes.all(), "cartid": cartId})

def create_list(request):
    cartId = request.GET.get('cartid')
    thisCart = Cart.objects.get(pk=cartId)
    return render(request, 'create_list.html')