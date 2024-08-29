from rest_framework import serializers

from .models import Tilibizde

from apps.categories.serializers import CategorySerializer


class TilibizdeCardSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)    

    class Meta:
        model = Tilibizde
        fields = ('photo', 'title', 'category', 'created_at', )


class TilibizdeDetailedViewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Tilibizde
        fields = ('photo', 'title', 'description', 'photo2', 'description2', 'category', 'created_at', )