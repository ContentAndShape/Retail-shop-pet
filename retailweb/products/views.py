from django.shortcuts import render

from .models import Product


def categories(request):
    return render(request, 'products/categories.html')


def index(request, product_category, page_number):
    items_per_page = 12
    products_query = Product.objects.filter(
        category=product_category).order_by('-id')
    filtered_query = filter_quantity(
        products_query, items_per_page, page_number)
    grouped_products_list = group_by_four(filtered_query)
    context = {
        'grouped_products_list': grouped_products_list,
        'product_category': product_category,
    }

    return render(request, 'products.html', context)


def selected_product(
    request, product_category, 
    page_number, selected_prod_id):
    product_query = Product.objects.get(id=selected_prod_id)
    context = {
        'product': product_query,
    }

    return render(request, 'selected_product.html', context)


# Returns a QuerySet with determined quantity of elements (items_quantity)
def filter_quantity(query, items_quantity, page):
    end = page * items_quantity
    start = end - items_quantity
    
    return(query[start:end])


# Returns a list of tuples from the iterable argument
# This case creates tuples with 4 elements
def group_by_four(iter):
    iter = list(iter)

    try:
        return [(iter[i], iter[i + 1], iter[i + 2], iter[i + 3]) for i 
            in range(0, len(iter), 4)]

    # If the number of elements < 4:
    except IndexError:
        iter.append(None)
        return group_by_four(iter)
