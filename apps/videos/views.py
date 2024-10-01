from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
