from django.db import models
from recipes.models import Recipe


class review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='aynonomous')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'review'