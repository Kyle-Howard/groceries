from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.TextField()
    recipe_id = models.IntegerField()
    
    def __str__(self):
        return F"{self.recipe_id} - {self.recipe_name}"

class Cart(models.Model):
    recipes = models.ManyToManyField(Recipe)