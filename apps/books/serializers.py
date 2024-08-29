from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
        ref_name = 'BookCategorySerializer'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'photo', 'title', 'description', 'category', 'file')


    