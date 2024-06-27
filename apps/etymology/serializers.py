# etymology/serializers.py
from rest_framework import serializers
from .models import Etymology

class EtymologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Etymology
        fields = ('id', 'photo', 'title', 'category', 'description')