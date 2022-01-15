from os import name
from django.shortcuts import render

from django.http import HttpResponse

from .models import Product

def index(request):
    prod = Product.objects.filter(name='test_hat')
    output = f'{prod[0].name}'
    return HttpResponse(output)
