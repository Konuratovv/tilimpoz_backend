# etymology/serializers.py
from rest_framework import serializers

from .models import Etymology
from apps.categories.serializers import CategorySerializer

class EtymologySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Etymology
        fields = ('photo', 'title', 'category', 'created_at', )


class EtymologyDetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Etymology
        fields = ('image', 'title', 'description', 'photo2', 'description2' 'category', 'created_at')        