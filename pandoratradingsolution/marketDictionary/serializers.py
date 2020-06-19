from rest_framework import serializers
from .models import Ticker

class TickerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    short_name = serializers.CharField(max_length=20)
    full_name = serializers.CharField(max_length=300)
    market_id = serializers.IntegerField()
    site = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Ticker.objects.create(**validated_data)