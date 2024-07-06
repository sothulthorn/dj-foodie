from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Recipe

# Create your views here.
def recipes(request):
  recipes = Recipe.objects.all()
  context = {"recipes": recipes}

  
  return render(request, "recipes/recipes.html", context)

def recipe(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  context = {"recipe": recipe}
  
  return render(request, "recipes/recipe.html", context)