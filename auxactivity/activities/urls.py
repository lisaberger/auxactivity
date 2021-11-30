from django.urls import path
from .views import activity_overview, add_activity_view

#Eigene URLs für Aktivitäten
urlpatterns = [
    path('', activity_overview, name="startpage"),
    path('activities/', activity_overview, name="activity_overview"),
    path('newactivity/', add_activity_view, name="add_activity"),
]