from datetime import date

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(User, related_name='re_participants', null=True)
    image = models.ImageField('Activities', upload_to="activities", default="activities/activity_default_placeholder.png")
    location = models.CharField(max_length=300, default="Augsburg")
    date = models.DateField(default=date.today, null=True, blank=True)

    def __str__(self):
        return self.name




