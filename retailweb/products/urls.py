from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<slug:product_category>/', views.index),
]
