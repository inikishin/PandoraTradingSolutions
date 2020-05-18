from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Ticker, Market


def index(request):
    ticker_list = Ticker.objects.order_by('short_name')
    context = {'ticker_list': ticker_list}
    return render(request, 'marketDictionary/index.html', context)


def detail(request, ticker_id):
    ticker = get_object_or_404(Ticker, pk=ticker_id)
    return render(request, 'marketDictionary/detail.html', {'ticker': ticker})
