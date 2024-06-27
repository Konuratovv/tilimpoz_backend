from rest_framework import serializers
from .models import Tilibizde

class TilibizdeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tilibizde
        fields = ('id', 'photo', 'title', 'category', 'description')