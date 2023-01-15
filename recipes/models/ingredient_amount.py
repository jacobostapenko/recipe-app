from django.db import models

from recipes.models import Recipe, Ingredient


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    unit = models.CharField(max_length=50, blank=True, null=True)  # pounds, lbs, oz ,grams, etc

    def __str__(self):
        return str(self.ingredient) + ' ' + str(self.amount)

    class Meta:
        db_table = 'recipeingredient'