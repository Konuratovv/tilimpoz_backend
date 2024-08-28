from rest_framework import generics
from rest_framework import permissions

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

from django_filters import rest_framework as filters


class BookViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = BookFilter
