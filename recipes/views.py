from django.shortcuts import render, HttpResponse
from . import models



# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    
    context = {
        'recipes':recipes
    }
    return render(request, 'recipes/home.html', context)#HttpResponse('<h1> welcome to app</h1>')

def about(request):
    return HttpResponse('<h1> this is a recipes app to find recipes</h1>')

def recipe(request):
    return render(request, 'recipes/recipe.html' )