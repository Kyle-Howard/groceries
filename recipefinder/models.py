from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_id = models.IntegerField(null=True)
    amount = models.FloatField(null=True)
    unit = models.TextField()
    name = models.TextField()

class Recipe(models.Model):
    recipe_name = models.TextField()
    recipe_id = models.IntegerField(null=True)
    servings = models.IntegerField(null=True)
    time_required = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return F"{self.recipe_name} - {self.recipe_id}"

class Cart(models.Model):
    recipes = models.ManyToManyField(Recipe)