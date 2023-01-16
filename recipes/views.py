from django.shortcuts import render, HttpResponse
from . import models



# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    reviews = models.review.objects.all().last()
    context = {
        'recipes':recipes,
        'reviews':reviews
    }
    if request.method == 'POST':
        if request.POST.get('review'):
            post=models.review()
            post.message= request.POST.get('review')
            post.save()

    return render(request, 'recipes/home.html', context)#HttpResponse('<h1> welcome to app</h1>')

def about(request):
    return HttpResponse('<h1> this is a recipes app to find recipes</h1>')

def recipe(request):
    return render(request, 'recipes/recipe.html' )