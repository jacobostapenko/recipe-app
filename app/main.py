from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max=100)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
