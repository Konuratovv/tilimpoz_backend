from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    category__title = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Book
        fields = ('category__title', )