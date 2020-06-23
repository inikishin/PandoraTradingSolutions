from django import template
from django.utils.safestring import mark_safe
import markdown
from datetime import timedelta

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name='predictiondate')
def predictiondate_format(text, lag):
    predictiondate = text + timedelta(days=lag)
    return predictiondate

@register.filter(name='predictionprice')
def predictiondate_format(text, percCh):
    if text != 0:
        predictiondate = '{0} ({1}%)'.format(round(text, 2), round(percCh, 1))
    else:
        predictiondate = 'Нет данных'
    return predictiondate

@register.filter(name='predictionproba')
def predictionproba_format(text):
    if text != 0:
        predictiondate = 'Prob.: {0}%'.format(round(text*100, 1))
    else:
        predictiondate = ''
    return predictiondate