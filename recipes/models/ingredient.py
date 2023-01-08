from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    # just to keep track of when stuff was created. just good practice
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ingredient'
