from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(Category, blank=False)  # Allows multiple categories

    def __str__(self):
        return self.name
