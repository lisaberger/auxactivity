from django.urls import path
from .views import activity_overview

#Eigene URLs für Aktivitäten
urlpatterns = [
    path('', activity_overview),
    path('activities/', activity_overview)
]