from rest_framework import serializers
from .models import Book, BookCategory

from apps.categories.serializers import CategorySerializer

class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ('id', 'title', )
        ref_name = 'BookCategorySerializer'


class BookSerializer(serializers.ModelSerializer):
    book_category = BookCategorySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'photo', 'title', 'author', 'year', 'book_category', 'category', 'file')


class BookDetailedSerializer(serializers.ModelSerializer):
    book_category = BookCategorySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'photo', 'title', 'description', 'author', 'year', 'book_category', 'category', 'file')


    