from django import template


register = template.Library()


@register.filter(name='snippet')
def snippet(value):
    return value[:35] + "\t..."