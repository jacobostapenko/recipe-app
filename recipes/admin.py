from django.contrib import admin
from recipes.models import Recipe, Ingredient, RecipeIngredient

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)