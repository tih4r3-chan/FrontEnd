from django.urls import path
from django.contrib.auth import views as  auth_views
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]