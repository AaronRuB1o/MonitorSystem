from django import template
import json
register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(obj, attr_name):
    """
    Custom template filter to fetch attribute dynamically using getattr
    """
    try:
        return getattr(obj, attr_name, '')
    except AttributeError:
        return ''
    
@register.filter
def to_json(value):
    return json.dumps(value)