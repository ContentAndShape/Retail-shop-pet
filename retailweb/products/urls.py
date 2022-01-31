from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<slug:product_category>/<int:page_number>/', views.index),
    path('<slug:product_category>/<int:page_number>/<int:selected_prod_id>/',
        views.selected_product)
]
