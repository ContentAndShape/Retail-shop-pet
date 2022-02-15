from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_categories, name='products_categories'),
    path('<slug:selected_gender>/<slug:selected_category>/', views.index),
    path('<slug:selected_gender>/<slug:selected_category>/<int:selected_prod_id>/',
        views.selected_product, name='selected_product'),
]
