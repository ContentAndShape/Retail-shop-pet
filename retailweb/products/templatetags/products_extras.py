from os import name
from urllib.parse import urlencode

from django import template

register = template.Library()


# This tag adds a query string before the new param
# Usage: {% saved_query "param=" value %}
@register.simple_tag(name='saved_query')
def saved_query(query_set_list, param, value):
    query_dict = dict(query_set_list)
    query_dict[param] = value
    
    return urlencode(query_dict)
