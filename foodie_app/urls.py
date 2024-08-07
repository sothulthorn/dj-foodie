from django.urls import path
from . import views


app_name = "foodie_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/<int:category_id>/", views.recipes, name="recipes"),
    path("add-category/", views.add_category, name="add_category"),
    path("add-recipe/", views.add_recipe, name="add_recipe_no_genre"),
    path("add-recipe/category/<int:category_id>/", views.add_recipe, name="add_recipe_with_genre")
]
