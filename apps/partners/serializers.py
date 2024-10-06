from rest_framework import serializers

from . import models

class PartnersSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Partner
        fields = ('id', 'photo')