from django.shortcuts import render
from products.models import Product

def index(request):
    recent_items = Product.objects.order_by('-id')[:5]
    context = {
        'recent_items': recent_items,
    }
    return render(request, 'homepage/index.html', context)


def about(request):
    return render(request, 'homepage/about.html')
