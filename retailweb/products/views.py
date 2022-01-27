from django.shortcuts import render

from .models import Product


def categories(request):
    return render(request, 'products/categories.html')


def index(request, product_category):
    products_query = Product.objects.filter(
        category=product_category).order_by('-id') # newest models first
    grouped_products_list = group_by_four(products_query)
    context = {
        'grouped_products_list': grouped_products_list,
        'product_category': product_category,
    }
    return render(request, 'products.html', context)


def selected(request, product_category, selected_prod_id):
    product_query = Product.objects.get(id=selected_prod_id)
    context = {
        'selected_product': product_query,
        'product_category': product_category,
    }
    return render(request, 'selected_product.html', context)

# Returns the list of tuples from the iterable argument
def group_by_four(iter):
    iter = list(iter)

    try:
        return [(iter[i], iter[i + 1], iter[i + 2], iter[i + 3]) for i 
            in range(0, len(iter), 4)]
    # If the number of elements < 4:
    except IndexError:
        iter.append(None)
        return group_by_four(iter)
