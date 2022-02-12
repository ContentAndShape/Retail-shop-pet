from urllib.parse import urlencode

from django import template

register = template.Library()


# Usage: {% saved_query "additional_param" value %}
# Preserves existing params when adding new one or changing existing
@register.simple_tag(name='saved_query')
def saved_query(query_set_list, param, value):
    query_dict = dict(query_set_list)
    query_dict[param] = value
    
    return urlencode(query_dict)
