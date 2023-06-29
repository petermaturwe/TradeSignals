from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def normalize_decimal(value):
    if isinstance(value, Decimal):
        return format(value.normalize(), 'g')
    return value
