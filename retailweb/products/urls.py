from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<slug:selected_category>/', views.index),
    path('<slug:selected_category>/<int:selected_prod_id>/',
        views.selected_product),
]
