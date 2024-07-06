from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView

from recipes.models import Recipe
from sandbox.form import FeedbackForm
from sandbox.models import Feedback

# Create your views here.
def index(request):
  recipes = Recipe.objects.all()
  
  context = {"recipes": recipes}
  return render(request, "sandbox/index.html", context)

class RecipeListView(ListView):
  model = Recipe
  template_name = "sandbox/index.html"
  context_object_name = "recipes"
  
  def get_queryset(self):
    filtered_recipes = Recipe.objects.filter(category__name__iexact="soup")
    return filtered_recipes

class RecipeDetailView(DetailView):
  model = Recipe
  template_name = "sandbox/recipe_detail.html"
  context_object_name = "recipe"
  
class SpecificRecipesView(View):
  def get(self, request, *args, **kwargs):
    # fetch recipes with 'refreshing" in the description
    refreshing_recipes = Recipe.objects.filter(description__icontains="refreshing")
    context = {"refreshing": refreshing_recipes}
    return render(request, "sandbox/refreshing_recipe.html", context)
  
def thank_you(request):
  return HttpResponse("Thank you for your feedback")
  
def feedback(request):
  if request.method == "POST":
    form = FeedbackForm(request.POST)
    if form.is_valid():
      # process the form
      print(form.cleaned_data)
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      feedback = form.cleaned_data["feedback"]
      satisfaction = form.cleaned_data["satisfaction"]
      Feedback.objects.create(
        name=name,
        email=email,
        feedback=feedback,
        satisfaction=satisfaction
      )
      return redirect('sandbox:thank_you')
  else:
    form = FeedbackForm()
    
  context = {"form": form}
  return render(request, "sandbox/feedback_form.html", context)