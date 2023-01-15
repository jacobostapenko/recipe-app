from django.db import models

from recipes.models import Recipe, Ingredient


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.ingredient) + ' ' + str(self.amount)

    class Meta:
        db_table = 'recipeingredient'