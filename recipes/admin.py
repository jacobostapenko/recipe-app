from django.contrib import admin
from recipes.models import Recipe, Ingredient, IngredientAmount

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)