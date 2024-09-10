from django_filters import rest_framework as filters
from .models import Test

class TestFilter(filters.FilterSet):
    category__title = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Test
        fields = ('category__title', )