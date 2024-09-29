from rest_framework import serializers
from .models import Category, SearchHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', )
        ref_name = 'ArticleCategorySerializer'
        

class SearchHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SearchHistory
        fields = ('id', 'query', )