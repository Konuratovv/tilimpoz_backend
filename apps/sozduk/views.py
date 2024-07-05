from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Sozduk
from .serializers import SozdukSerializer

class SozdukViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sozduk.objects.all()
    serializer_class = SozdukSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
