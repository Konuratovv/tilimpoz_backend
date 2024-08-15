from rest_framework import serializers
from .models import SabattuuModel


class SabattuuJoobtorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SabattuuModel
        fields = ('title', 'image', 'created_at', )


class SabattuuJoobtorDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = SabattuuModel
        fields = ('image', 'title', 'description', 'created_at')