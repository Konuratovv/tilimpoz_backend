from rest_framework import serializers
from .models import TestCategory, Test

class TestCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = TestCategory
        fields = ('title', )


class TestSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Test
        fields = ('image', 'title', )

        