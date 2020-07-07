from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Ticker, Market
from dailyAnalysis.models import Post
from predictions.models import Prediction


def index(request):
    ticker_list = Ticker.objects.order_by('short_name')
    context = {'ticker_list': ticker_list}
    return render(request, 'marketDictionary/index.html', context)


def detail(request, ticker_id):
    ticker = get_object_or_404(Ticker, pk=ticker_id)

    post_list = Post.objects.order_by('-date_analysis').filter(ticker__exact=ticker_id)
    prediction_ticker_list = Prediction.objects.filter(ticker__exact=ticker_id).order_by('-created')

    return render(request, 'marketDictionary/detail.html', {'ticker': ticker, 'post_list': post_list, 'prediction_ticker_list': prediction_ticker_list})

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
