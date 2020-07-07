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
