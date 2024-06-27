from rest_framework import serializers
from .models import Sozduk

class SozdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sozduk
        fields = ('id', 'category', 'word', 'translation')