from rest_framework import serializers
from .models import Rule

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('id', 'title', 'description', 'author', 'created_at')

class RuleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('id', 'title', 'author', 'created_at')