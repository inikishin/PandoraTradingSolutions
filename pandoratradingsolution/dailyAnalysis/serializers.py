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

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
