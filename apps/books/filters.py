from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    book_category__title = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Book
        fields = ('book_category__title', )
        
    def filter_book_category_title(self, queryset, name, value):
        if value.lower() == "бардыгы":
            return queryset
        return queryset.filter(book_category__title__icontains=value)