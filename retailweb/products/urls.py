from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<slug:product_category>/', views.index),
    path('<slug:product_category>/<int:selected_prod_id>', views.selected),
]
