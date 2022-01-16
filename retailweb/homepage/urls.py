from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='about'),
]