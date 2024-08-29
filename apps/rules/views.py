from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Rule
from .serializers import RuleSerializer, RuleCardSerializer

class RuleListAPIView(generics.ListAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]