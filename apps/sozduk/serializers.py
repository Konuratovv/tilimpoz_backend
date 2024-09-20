from rest_framework import serializers
from .models import SozdukCategory, Sozduk

from apps.categories.serializers import CategorySerializer

class SozdukSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SozdukCategory
        fields = ('id', 'title', 'photo', 'category', )

class SozdorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sozduk
        fields = ('id', 'word', 'translation', 'image', )