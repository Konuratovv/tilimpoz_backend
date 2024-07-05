from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Tilibizde
from .serializers import TilibizdeSerializer

class TilibizdeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tilibizde.objects.all()
    serializer_class = TilibizdeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]