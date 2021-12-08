from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

# Klasse Aktivitäten

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    categories = models.ManyToManyField(Category)




