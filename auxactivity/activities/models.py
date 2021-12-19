from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    categories = models.ManyToManyField(Category)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(User, related_name='re_participants', null=True)

    def __str__(self):
        return self.name




