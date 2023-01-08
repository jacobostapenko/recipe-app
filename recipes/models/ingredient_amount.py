from django.db import models

from recipes.models import Recipe, Ingredient


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredientamount'