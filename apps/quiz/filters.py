from django_filters import rest_framework as filters
from .models import Test

class TestFilter(filters.FilterSet):
    category__title = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Test
        fields = ('category__title', )
        
    def filter_category_title(self, queryset, name, value):
        if not value or value.lower() == 'бардыгы':
            return queryset
        return queryset.filter(category__title__icontains=value)