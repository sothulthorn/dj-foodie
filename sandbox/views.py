from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  data = ["Pizza", "Pasta", "Bread", "Salad"]
  # data = []
  
  context = {"foods": data}
  return render(request, "sandbox/index.html", context)