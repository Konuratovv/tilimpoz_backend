from rest_framework import serializers
from .models import Rule, RuleCard

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('id', 'title', 'description')

class RuleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleCard
        fields = ('id', 'title', 'author', 'date', 'rule')