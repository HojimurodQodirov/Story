from django.urls import path
from .views import PostListAPIView, DetailedInfoListAPIView, DetailedInfoDetailAPIView


urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('detailed_infos/', DetailedInfoListAPIView.as_view(), name='detailedinfo-list'),
    path('detailed_info/<int:pk>/', DetailedInfoDetailAPIView.as_view(), name='detailed_info_detail'),
]
