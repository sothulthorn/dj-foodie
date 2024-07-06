from django.urls import path
from . import views
from sandbox.views import RecipeDetailView, RecipeListView, SpecificRecipesView

app_name = "sandbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("refreshing/", views.SpecificRecipesView.as_view(), name="refreshing_recipes"),
    path("feedback", views.feedback, name="feedback"),
    path("thank-you", views.thank_you, name="thank_you")
]
