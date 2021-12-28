#Eigene URLs für Startseite
from django.urls import path
from startpage.views import startpage_view

urlpatterns = [
    path('', startpage_view, name="startpage"),
]