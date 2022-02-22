from urllib.parse import urlparse, parse_qsl

from django.shortcuts import get_object_or_404, render

from products.models import Product


def search(request):
    query_string = urlparse(request.get_full_path())[4]
    query_dict = dict(parse_qsl(query_string))
    requested_id = query_dict['id']

    searched_item = get_object_or_404(Product, id=requested_id)

    context = {
        'item': searched_item,
        'query_dict': query_dict,
    }

    return render(request, 'search_index.html', context)

