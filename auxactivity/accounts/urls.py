from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import login_view, logout_view, register_view

#Eigene URLs für Aktivitäten
urlpatterns = [
    path('login', LoginView.as_view(), name="login_url"),
    path('logout', LogoutView.as_view(), name="logout_url"),
    path('register', register_view, name="register_url"),
]
