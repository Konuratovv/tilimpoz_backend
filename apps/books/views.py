from urllib.parse import unquote

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .models import Book, BookCategory
from .serializers import BookSerializer, BookDetailedSerializer, CategorySerializer
from .filters import BookFilter

from django_filters import rest_framework as filters

class BookCategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = BookCategory.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        serialized_data = []
        serialized_data += [{'id': 0, 'title': 'Бардыгы'}]
        serialized_data += self.get_serializer(self.get_queryset(), many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class BookViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = BookFilter


class BookDetailedAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

