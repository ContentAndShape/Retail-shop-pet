from urllib.parse import parse_qsl, urlparse

from django.shortcuts import render

from .models import Product


def categories(request):
    return render(request, 'products/categories.html')


def index(request, selected_category):
    query_set_list = parse_qsl(urlparse(request.get_full_path())[4])
    
    page = get_std_params(request)['page']
    show_recent = get_std_params(request)['show-recent']
    items_per_page = get_std_params(request)['items']

    if show_recent == 1:
        general_query = Product.objects.filter(
            category=selected_category).order_by('-id')
    else:
        general_query = Product.objects.filter(
            category=selected_category).order_by('id')

    if page == 1:
        prev_page = None
    else:
        prev_page = page - 1

    filtered_query = filter_by_quantity(
        general_query, items_per_page, page)
    grouped_products = group_by_four(filtered_query)
    context = {
        'products_list': grouped_products,
        'category': selected_category,
        'page': page,
        'next_page': page + 1,
        'prev_page': prev_page,
        'query_list': query_set_list,
    }

    return render(request, 'products.html', context)


def selected_product(request, selected_category, selected_prod_id):
    product_query = Product.objects.get(id=selected_prod_id)
    context = {
        'product': product_query,
    }

    return render(request, 'selected_product.html', context)


# Determines the total # of items to render on a single page
def filter_by_quantity(query_set, items_quantity, page):
    end = page * items_quantity
    start = end - items_quantity
    
    return(query_set[start:end])


# Returns a list of tuples from an iterable arg
# In this case each tuple contain 4 elements
def group_by_four(iter):
    iter = list(iter)

    try:
        return [(iter[i], iter[i + 1], iter[i + 2], iter[i + 3]) for i 
            in range(0, len(iter), 4)]

    # If the number of elements < required:
    except IndexError:
        iter.append(None)
        return group_by_four(iter)


# Checks if any val of param is provided, if so - assigns new val
# if not - provide std val
def get_std_params(request):
    #std param-val pairs
    filters = {
        'page': 1,
        'items': 12,
        'show-recent': 1,
    }
    output = {}

    for param in filters:
        value = int(filters.get(param))

        if param not in request.GET: #uses std val
            output[param] = value
        else: #replaces std val with provided one
            provided_val = int(request.GET.get(param))
            output[param] = provided_val
    
    return output
