from rest_framework import serializers
from .models import SabattuuModel

from apps.categories.serializers import CategorySerializer


class SabattuuJoobtorListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SabattuuModel
        fields = ('title', 'image', 'category', 'created_at', )


class SabattuuJoobtorDetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SabattuuModel
        fields = ('image', 'title', 'description', 'photo2', 'description2' 'category', 'created_at')