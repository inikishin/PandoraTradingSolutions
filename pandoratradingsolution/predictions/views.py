from datetime import datetime

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Prediction, PredictionHorizon
import marketDictionary.models as md

def index(request):
    ticker_list = md.Ticker.objects.order_by('short_name')
    prediction_list = []
    for t in ticker_list:
        prediction_ticker_list = Prediction.objects.filter(ticker__exact=t.id).order_by('created')
        ticker_prediction = {"ticker": t}
        for p in prediction_ticker_list:
            ticker_prediction.update({p.horizon.horizon_name: {
                                                                'created': p.created,
                                                                'horizon': p.horizon,
                                                                'predictprice': p.predictprice,
                                                                'prctChange': p.prctChange,
                                                                'probability': p.probability
                                                                }})

        prediction_list.append(ticker_prediction)

    paginator = Paginator(prediction_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    #context = {'prediction_list': prediction_list}

    return render(request, 'predictions/index.html', context)

# API
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PredictionSerializer, PredictionHorizonSerializer

class PredictionHorizonView(APIView):
    def get(self, request):
        horizons = PredictionHorizon.objects.all()
        serializer = PredictionHorizonSerializer(horizons, many=True)
        return Response({"horizons": serializer.data})

class PredictionView(APIView):
    def get(self, request):
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response({"predictions": serializer.data})

    def post(self, request):
        prediction = request.data.get('prediction')
        serializer = PredictionSerializer(data=prediction)
        if serializer.is_valid(raise_exception=True):
            prediction_saved = serializer.save()
        return Response({"success": "Prediction id '{}' created successfully".format(prediction_saved.id)})