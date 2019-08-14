from django.db import models

# Create your models here.
# class Ingredient(models.Model):
#     ingredient_id = models.IntegerField()
#     amount = models.IntegerField()
#     unit = models.CharField()
#     name = models.TextField()

class Recipe(models.Model):
    recipe_name = models.TextField()
    recipe_id = models.IntegerField()
    # servings = models.IntegerField()
    # time_required = models.IntegerField()
    # rating = models.FloatField()
    # ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return F"{self.recipe_name} - {self.recipe_id}"

class Cart(models.Model):
    recipes = models.ManyToManyField(Recipe)