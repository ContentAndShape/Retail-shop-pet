from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.search_brand, name='search_brand'),
]
