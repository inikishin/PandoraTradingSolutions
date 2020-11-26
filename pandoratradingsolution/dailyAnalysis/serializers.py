from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    analysis_type_id = serializers.IntegerField()
    ticker_id = serializers.IntegerField()
    date_analysis = serializers.DateField()
    post_img = serializers.CharField()
    post_description = serializers.CharField()
    header = serializers.CharField()
    content = serializers.CharField()
    slug = serializers.SlugField()
    slug_url = serializers.SlugField()
    created = serializers.DateTimeField()
    sig_elder = serializers.IntegerField()
    sig_channel = serializers.IntegerField()
    sig_DivBar = serializers.IntegerField()
    sig_NR4ID = serializers.IntegerField()
    sig_breakVolatility = serializers.IntegerField()
    sig_elder_proba = serializers.FloatField()
    sig_channel_proba = serializers.FloatField()
    sig_DivBar_proba = serializers.FloatField()
    sig_NR4ID_proba = serializers.FloatField()
    sig_breakVolatility_proba = serializers.FloatField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)