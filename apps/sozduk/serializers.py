from rest_framework import serializers
from .models import SozdukCategory, Sozduk

from apps.categories.serializers import CategorySerializer

class SozdukSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SozdukCategory
        fields = ('id', 'title', 'photo', 'category', )
        
class SozdukForSozdorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SozdukCategory
        fields = ('id', 'title')

class SozdorSerializer(serializers.ModelSerializer):
    category = SozdukForSozdorSerializer()

    class Meta:
        model = Sozduk
        fields = ('id', 'word', 'translation', 'photo', 'category')