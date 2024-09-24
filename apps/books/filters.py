from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    book_category = filters.CharFilter(method='filter_book_category')


    class Meta:
        model = Book
        fields = ('book_category', )
        
    def filter_book_category(self, queryset, name, value):
        if value is None or value.lower() == 'бардыгы':
            return queryset
        return queryset.filter(book_category__title__icontains=value)