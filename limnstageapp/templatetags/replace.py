from django import template
import re
register = template.Library()

@register.filter
def replace(value):
    return re.sub('[^A-Za-z0-9]+', '-', value)