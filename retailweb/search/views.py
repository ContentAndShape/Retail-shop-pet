from django.http import QueryDict

from django.shortcuts import get_object_or_404, render

from products.models import Product


def search(request):
    query_string = request.META['QUERY_STRING']
    query_dict = QueryDict(query_string).dict()
    requested_id = query_dict['id']
    searched_item = get_object_or_404(Product, id=requested_id)

    context = {
        'item': searched_item,
        'query_dict': query_dict,
    }

    return render(request, 'search_index.html', context)

