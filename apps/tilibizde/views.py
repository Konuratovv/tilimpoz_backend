from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Tilibizde
from .serializers import TilibizdeCardSerializer, TilibizdeDetailedViewSerializer

class TilibizdeCardsAPIView(generics.ListAPIView):
    queryset = Tilibizde.objects.all()
    serializer_class = TilibizdeCardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TilibizdeDetailedAPIView(generics.RetrieveAPIView):
    queryset = Tilibizde.objects.all()
    serializer_class = TilibizdeDetailedViewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
