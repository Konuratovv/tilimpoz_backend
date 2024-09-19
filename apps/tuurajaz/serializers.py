# etymology/serializers.py
from rest_framework import serializers

from .models import TuuraJazModel
from apps.categories.serializers import CategorySerializer

class TuuraJazSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)


    class Meta:
        model = TuuraJazModel
        fields = ('photo', 'title', 'category', 'created_at', )


class TuuraJazDetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = TuuraJazModel
        fields = ('photo', 'title', 'description', 'photo2', 'description2', 'category', 'created_at', )        