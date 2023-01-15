from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('about/', views.about, name='recipes-about'),
    #TODO: delete
    path('SpecificRecipe/', views.recipe, name='recipe')

]