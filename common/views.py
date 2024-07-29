from rest_framework import generics
from .models import Post, DetailedInfo
from .serializers import PostSerializer, DetailedInfoSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailedInfoListAPIView(generics.ListCreateAPIView):
    queryset = DetailedInfo.objects.all()
    serializer_class = DetailedInfoSerializer


class DetailedInfoDetailAPIView(generics.RetrieveAPIView):
    queryset = DetailedInfo.objects.all()
    serializer_class = DetailedInfoSerializer
