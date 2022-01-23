from django.shortcuts import render
from products.models import Product

def index(request):
    return render(request, 'homepage/index.html')


def about(request):
    return render(request, 'homepage/about.html')
