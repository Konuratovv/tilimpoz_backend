from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Document
from .serializers import DocumentSerializer

class DocumentListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
