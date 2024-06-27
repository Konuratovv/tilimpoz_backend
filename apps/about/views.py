from rest_framework import generics
from .models import About
from .serializers import AboutSerializer

class AboutListCreateAPIView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

