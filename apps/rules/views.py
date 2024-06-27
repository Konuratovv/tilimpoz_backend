from rest_framework import generics
from .models import Rule
from .serializers import RuleSerializer

class RuleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
