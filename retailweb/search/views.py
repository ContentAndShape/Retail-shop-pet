from urllib.parse import urlparse, parse_qsl

from django.shortcuts import get_object_or_404, render

from products.models import Product

def search(request):
    query_string = urlparse(request.get_full_path())[4]
    query_dict = dict(parse_qsl(query_string))

    general_db_query = 

    context = {

    }

    return render()

