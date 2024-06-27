from rest_framework import generics
from .models import Tilibizde
from .serializers import TilibizdeSerializer

class TilibizdeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tilibizde.objects.all()
    serializer_class = TilibizdeSerializer

