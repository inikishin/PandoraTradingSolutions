from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Ticker, Market
from dailyAnalysis.models import Post
from predictions.models import Prediction

@xframe_options_exempt
def index(request):
    ticker_list = Ticker.objects.order_by('short_name')

    paginator = Paginator(ticker_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'marketDictionary/ms_index.html', context)

@xframe_options_exempt
def detail_slug(request, ticker_name):
    ticker = get_object_or_404(Ticker, short_name=ticker_name.upper())

    post_list = Post.objects.order_by('-date_analysis').filter(ticker__exact=ticker.id)
    #prediction_ticker_list = Prediction.objects.filter(ticker__exact=ticker.id).order_by('-created')

    prediction_ticker_list = Prediction.objects.filter(ticker__exact=ticker.id).order_by('created')
    ticker_prediction = {"ticker": ticker}
    prediction_list = []
    for p in prediction_ticker_list:
        ticker_prediction.update({p.horizon.horizon_name: {
                                                            'created': p.created,
                                                            'horizon': p.horizon,
                                                            'predictprice': p.predictprice,
                                                            'prctChange': p.prctChange,
                                                            'probability': p.probability
                                                            }})

    prediction_list.append(ticker_prediction)

    return render(request, 'marketDictionary/ms_ticker.html', {'ticker': ticker,
                                                               'post_list': post_list[:3],
                                                               'prediction_ticker_list': prediction_list,
                                                               'post_count': len(post_list),
                                                               'prediction_count': len(prediction_ticker_list)})
# API


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TickerSerializer


class TickerView(APIView):
    def get(self, request):
        tickers = Ticker.objects.all()
        serializer = TickerSerializer(tickers, many=True)
        return Response({"tickers": serializer.data})

    def post(self, request):
        ticker = request.data.get('ticker')
        # Create an ticker from the above data
        serializer = TickerSerializer(data=ticker)
        if serializer.is_valid(raise_exception=True):
            ticker_saved = serializer.save()
        return Response({"success": "Ticker '{}' created successfully".format(ticker_saved.short_name)})
