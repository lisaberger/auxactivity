#Eigene URLs für Startseite
from django.urls import path
from startpage.views import startpage_overview

urlpatterns = [
    path('', startpage_overview, name="startpage"),
]