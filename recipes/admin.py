from django.contrib import admin
from recipes.models import Recipe, Ingredient, RecipeIngredient, review

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(review)