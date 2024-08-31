from rest_framework import serializers
from .models import Document
from apps.categories.serializers import CategorySerializer

class DocumentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Document
        fields = ('id', 'title', 'photo', 'category', 'file')