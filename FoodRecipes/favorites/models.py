from django.db import models
from django.contrib.auth.models import User
from main.models import Recipes

# Create your models here.


class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
