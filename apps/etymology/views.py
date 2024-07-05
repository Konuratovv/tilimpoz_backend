from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Etymology
from .serializers import EtymologySerializer

class EtymologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Etymology.objects.all()
    serializer_class = EtymologySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

