from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Dom V.',
        'title': 'Meatballs',
        'content': 'Combine ingredients, form into balls, brown, then place in oven.',
        'date_posted': 'May 18th, 2022'
    }]

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    
    context = {
        'recipes':recipes
    }
    return render(request, 'recipes/home.html', context)#HttpResponse('<h1> welcome to app</h1>')

def about(request):
    return HttpResponse('<h1> this is a recipes app to find recipes</h1>')