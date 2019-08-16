from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_id = models.IntegerField(null=True)
    amount = models.FloatField(null=True)
    unit = models.TextField()
    name = models.TextField()

    def __str__(self):
        return F"{self.ingredient_id}"

    def __eq__(self, other):
        return self.ingredient_id == other.ingredient_id

    def __ne__(self, other):
        return self.ingredient_id != other.ingredient_id

class Recipe(models.Model):
    recipe_name = models.TextField()
    recipe_id = models.IntegerField(null=True)
    servings = models.IntegerField(null=True)
    time_required = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    instructions = models.TextField(null=True)
    image = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return F"{self.recipe_name}"

class Cart(models.Model):
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredient)