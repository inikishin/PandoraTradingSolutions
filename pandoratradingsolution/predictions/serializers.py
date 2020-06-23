from rest_framework import serializers
from .models import Prediction, PredictionHorizon

class PredictionHorizonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    horizon_name = serializers.CharField()
    lag = serializers.IntegerField()

class PredictionSerializer(serializers.Serializer):
    horizon_id = serializers.IntegerField()
    ticker_id = serializers.IntegerField()
    created = serializers.DateField()
    currentprice = serializers.FloatField()
    predictprice = serializers.FloatField()
    prctChange = serializers.FloatField()
    probability = serializers.FloatField()

    def create(self, validated_data):
        return Prediction.objects.create(**validated_data)
