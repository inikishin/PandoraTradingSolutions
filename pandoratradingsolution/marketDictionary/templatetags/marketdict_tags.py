from django import template
from django.utils.safestring import mark_safe
import markdown
from datetime import timedelta

register = template.Library()

@register.filter(name='predictiondate')
def predictiondate_format(create_date, lag):
    predictiondate = create_date + timedelta(days=lag)
    return predictiondate

@register.filter(name='round_num')
def round_num_format(n, digits):
    rounded_number = round(n, digits)
    return rounded_number

@register.filter(name='content_preview')
def content_preview(text):
    preview = text.split('\n')[1]
    return preview[:100] + '...'

@register.filter(name='get_color_for_pred')
def get_color_for_pred(perc_change):
    return 'color-success' if perc_change > 0 else 'color-danger'
