from rest_framework import serializers
from .models import Tilibizde

class TilibizdeCardSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Tilibizde
        fields = ('photo', 'title', 'created_at', )


class TilibizdeDetailedViewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Tilibizde
        fields = ('photo', 'title', 'description', 'created_at', )