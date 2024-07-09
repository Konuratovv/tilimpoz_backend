from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Rule, RuleCard
from .serializers import RuleSerializer, RuleCardSerializer

class RuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RuleCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RuleCard.objects.all()
    serializer_class = RuleCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]