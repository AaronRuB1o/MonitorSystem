# yourapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='custom_filter_name')
def custom_filter(value):
    # Your custom filter logic here
    return modified_value
