from urllib.parse import parse_qsl, urlparse

from django.shortcuts import get_object_or_404, render

from .models import Product


def products_categories(request):
    return render(request, 'products/categories.html')


def index(request, selected_gender, selected_category):
    query_string = urlparse(request.get_full_path())[4]
    page = get_param(request)['page']
    items_per_page = get_param(request)['items']
    brand = get_param(request)['brand']
    sort_parameter_dict = resolve_sort_params(query_string)

    general_db_query = Product.objects.filter(
        category=selected_category,
        gender=selected_gender,
    )

    if brand:
        general_db_query = general_db_query.filter(name=brand)

    if 'show-recent' in sort_parameter_dict:
        if sort_parameter_dict['show-recent'] == '1':
            general_db_query = general_db_query.order_by('-id')
        if sort_parameter_dict['show-recent'] == '0':
            general_db_query = general_db_query.order_by('id')
    else:
        general_db_query = general_db_query.order_by('-id')

    if 'price' in sort_parameter_dict:
        if sort_parameter_dict['price'] == 'ascending':
            general_db_query = general_db_query.order_by('price')
        if sort_parameter_dict['price'] == 'descending':
            general_db_query = general_db_query.order_by('-price')

    # divides query into pages
    quantity_filtered_query = filter_by_quantity(
        general_db_query, items_per_page, page)
    grouped_by4_query = group_by_four(quantity_filtered_query)

    next_page = get_page_sequence(
        page, items_per_page, general_db_query)['next_page']
    prev_page = get_page_sequence(
        page, items_per_page, general_db_query)['prev_page']

    context = {
        'products_list': grouped_by4_query,
        'category': selected_category,
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'query_string': query_string,
        'brand': brand,
    }

    return render(request, 'products.html', context)


def selected_product(
    request, selected_gender, 
    selected_category, selected_prod_id):
    selected_product = get_object_or_404(Product, id=selected_prod_id)

    if selected_product.quantity == 0:
        stock = None
    else:
        stock = int(selected_product.quantity)

    context = {
        'product': selected_product,
        'stock': stock,
    }

    return render(request, 'selected_product.html', context)


# determines the num of items to render on a single page
def filter_by_quantity(query, items_quantity, page):
    end = page * items_quantity
    start = end - items_quantity
    
    return(query[start:end])


# takes an iterable arg and forms a list of tuples
# each tuple contain 4 elements
def group_by_four(iter):
    iter = list(iter)

    try:
        return [(iter[i], iter[i + 1], iter[i + 2], iter[i + 3]) for i 
            in range(0, len(iter), 4)]

    # If the number of elements < required:
    except IndexError:
        iter.append(None)
        return group_by_four(iter)


# compares params from request with params in "filters" ->
# -> merges them in one dict
def get_param(request):
    # Standard vals to use if they are not in request
    filters = {
        'page': 1,
        'items': 12,
        'show-recent': 1,
        'brand': None,
    }

    for param in filters:
        try: 
            value = int(filters.get(param))
        except TypeError:
            value = filters.get(param)

        if param not in request.GET:
            # uses standard val
            filters[param] = value
        else: 
            # uses given val
            try:
                given_val = int(request.GET.get(param))
                filters[param] = given_val
            except ValueError:
                given_val = request.GET.get(param)
                filters[param] = given_val
    
    return filters


def get_page_sequence(page_num, items_on_page, query):
    output = {}
    items_in_query = len(query)

    if page_num == 1:
        output['prev_page'] = None
    else:
        output['prev_page'] = page_num - 1

    if items_in_query % items_on_page:
        last_page = items_in_query // items_on_page + 1
    else:
        last_page = items_in_query // items_on_page

    if page_num == last_page:
        output['next_page'] = None
    else:
        output['next_page'] = page_num + 1

    return output


# returns the last added sorting param
def resolve_sort_params(qs):
    sort_params = [
    'show-recent',
    'price',
    ]
    output = {}
    query_dict = dict(parse_qsl(qs))
    sort_params_sequence = ()

    for param in sort_params:
        if param in query_dict:
            new_element = (param, )
            sort_params_sequence = sort_params_sequence + new_element

    # if no sort params
    if len(sort_params_sequence) == 0:
        return output

    winner_param = sort_params_sequence[-1]
    winner_val = query_dict[winner_param]
    output[winner_param] = winner_val

    return output
