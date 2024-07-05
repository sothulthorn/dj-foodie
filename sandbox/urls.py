from django.urls import path
from . import views

app_name = "sanbox"

urlpatterns = [
    path("", views.index)
]
