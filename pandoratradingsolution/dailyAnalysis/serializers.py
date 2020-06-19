from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    analysis_type_id = serializers.IntegerField()
    ticker_id = serializers.IntegerField()
    date_analysis = serializers.DateField()
    header = serializers.CharField()
    content = serializers.CharField()
    slug = serializers.SlugField()
    created = serializers.DateTimeField()
    sig_elder = serializers.IntegerField()
    sig_channel = serializers.IntegerField()
    sig_DivBar = serializers.IntegerField()
    sig_NR4ID = serializers.IntegerField()
    sig_breakVolatility = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
