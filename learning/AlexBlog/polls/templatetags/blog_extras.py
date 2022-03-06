from django import template
register = template.Library()

@register.filter()
def upper(value): #Only one argument
    """Converts a string into all uppercase"""
    return value.upper()
