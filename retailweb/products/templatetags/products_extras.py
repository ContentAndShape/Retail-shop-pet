from urllib.parse import urlencode

from django.http import QueryDict
from django import template

register = template.Library()


# usage: {% query_string "additional_param" value %}
# preserves existing filter params when adding new or changing existing
# if meets sorting param, replaces old (if existed) with the new one
@register.simple_tag(name='saved_query')
def saved_query(query_string, provided_param, provided_value):
    sort_params = [
    'show-recent',
    'price',
    ]
    query_dict = QueryDict(query_string).dict()

    if provided_param in sort_params:
        for elem in sort_params:
            if elem != provided_param:
                try:
                    # Delete others except provided
                    del query_dict[elem]
                except KeyError:
                    continue

    query_dict[provided_param] = provided_value
    
    return urlencode(query_dict)
