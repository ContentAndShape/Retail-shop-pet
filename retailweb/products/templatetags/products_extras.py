from urllib.parse import parse_qsl, urlencode

from django import template

register = template.Library()


# Usage: {% query_string "additional_param" value %}
# Preserves existing params when adding new one or changing existing
@register.simple_tag(name='saved_query')
def saved_query(query_string, provided_param, provided_value):
    sort_params = [
    'show-recent',
    'price',
    ]
    query_dict = dict(parse_qsl(query_string))

    if provided_param in sort_params:
        for elem in sort_params:
            if elem != provided_param:
                try:
                    del query_dict[elem]
                except KeyError:
                    continue

    query_dict[provided_param] = provided_value
    
    return urlencode(query_dict)
