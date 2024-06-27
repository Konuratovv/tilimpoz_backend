from rest_framework import generics
from .models import Sozduk
from .serializers import SozdukSerializer

class SozdukListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sozduk.objects.all()
    serializer_class = SozdukSerializer
