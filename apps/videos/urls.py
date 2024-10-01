from django.urls import path
from .views import VideoListAPIView, VideoDetailAPIView

urlpatterns = [
    path('', VideoListAPIView.as_view(), name='video-list'),
    path('<int:pk>/', VideoDetailAPIView.as_view(), name='video-detail'),
]
