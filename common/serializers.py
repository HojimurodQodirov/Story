from rest_framework import serializers
from .models import Post, DetailedInfo


class DetailedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedInfo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    detailed_info = DetailedInfoSerializer(many=True, read_only=True, source='detailedinfo_set')

    class Meta:
        model = Post
        fields = ['title', 'content', 'detailed_info', 'get_detailed_info_url']
