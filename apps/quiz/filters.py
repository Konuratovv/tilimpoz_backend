from django_filters import rest_framework as filters
from .models import Test

class TestFilter(filters.FilterSet):
    category__id = filters.CharFilter(method='filter_category_id')


    class Meta:
        model = Test
        fields = ('category__id', )
        
    def filter_category_id(self, queryset, name, value):
        if not value or value == '0':
            return queryset
        return queryset.filter(category__id=value)