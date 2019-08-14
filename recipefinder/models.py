from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.TextField()
    recipe_id = models.IntegerField()
    
    def __str__(self):
        return self.recipe_id

class Cart(models.Model):
    recipes = models.ManyToManyField(Recipe)