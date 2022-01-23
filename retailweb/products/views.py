from django.shortcuts import render

from .models import Product


def categories(request):
    return render(request, 'products/categories.html')


def index(request, product_category):
    products_list = Product.objects.filter(category=product_category)
    grouped_products_list = group_by_two(products_list)
    context = {
        'grouped_products_list': grouped_products_list,
        'product_category': product_category,
    }
    return render(request, 'products.html', context)

# Returns the list of tuples from the iterable argument
def group_by_two(iter):
    iter = list(iter)

    try:
        return [(iter[i], iter[i + 1]) for i in range(0, len(iter), 2)]
    # If the number of elements is odd:
    except IndexError:
        iter.append(None)
        return [(iter[i], iter[i + 1]) for i in range(0, len(iter), 2)]
