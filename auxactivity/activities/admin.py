from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Activity, Category

admin.site.register(Activity)
admin.site.register(Category)