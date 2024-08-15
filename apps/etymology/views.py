from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Etymology
from .serializers import EtymologySerializer, EtymologyDetailedSerializer

class EtymologyViewSet(generics.ListAPIView):
    queryset = Etymology.objects.all()
    serializer_class = EtymologySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class EtymologyDetailedAPIView(generics.RetrieveAPIView):
    queryset = Etymology.objects.all()
    serializer_class = EtymologyDetailedSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )



