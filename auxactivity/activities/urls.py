from django.urls import path
from .views import activity_overview, filter_form, add_activity_view, activity_detail_view

#Eigene URLs für Aktivitäten
urlpatterns = [
    path('activities/', activity_overview, name="activity_overview"),
    path('newactivity/', add_activity_view, name="add_activity"),
    path('choose/', filter_form, name='filter'),
    path('activity/<activity_id>', activity_detail_view, name='activity')
]