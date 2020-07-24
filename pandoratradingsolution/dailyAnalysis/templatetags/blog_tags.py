from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['attr_list']))


@register.filter(name='media_url')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, settings.MEDIA_URL)

@register.filter(name='signal')
def signal(value, arg):
    if value == 1:
        return 'Сигнал (' + str(round(arg*100, 2)) + '%)'
    else:
        return '-'

@register.filter(name='perc_format')
def signal(value):
    return str(round(value*100, 2)) + '%'

@register.filter(name='buysell_signal')
def buysell_signal(value):
    if value == 1:
        return 'Buy'
    elif value == -1:
        return 'Sell'
    else:
        return ''

@register.filter(name='price_color')
def price_color_format(price_change):
    if price_change > 0:
        col = 'color-success'
    elif price_change < 0:
        col = 'color-danger'
    else:
        col = 'color-primary'
    return col

@register.filter(name='icon_type')
def icon_type_format(price_change):
    if price_change > 0:
        col = 'fa fa-arrow-up'
    elif price_change< 0:
        col = 'fa fa-arrow-down'
    else:
        col = 'fa fa-arrow-right'
    return col