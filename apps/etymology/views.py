# etymology/views.py
from rest_framework import generics
from .models import Etymology
from .serializers import EtymologySerializer

class EtymologyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Etymology.objects.all()
    serializer_class = EtymologySerializer