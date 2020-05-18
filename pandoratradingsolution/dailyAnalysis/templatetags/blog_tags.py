from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter(name='media_url')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, settings.MEDIA_URL)