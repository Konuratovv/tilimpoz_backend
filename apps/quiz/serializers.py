from rest_framework import serializers

from . import models

from ..categories.serializers import CategorySerializer

class TestCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.TestCategory
        fields = ('id', 'title', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        extra_data = {'id': 0, 'title': 'Бардыгы'}
        return [extra_data] + [representation]


class TestListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    article = CategorySerializer()

    class Meta:
        model = models.Test
        fields = ('id', 'title', 'photo', 'article', 'questions_count')

    def get_questions_count(self, obj):
        return obj.questions.count()
    

class AnswerSeralizer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = models.Answer
        fields = ('id', 'answer', 'is_correct', 'points')

    def get_points(self, obj):
        return 1 if obj.is_correct else 0
    

class QuestionsListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = models.Question
        fields = ('id', 'question', 'answers')

    def get_answers(self, obj):
        return AnswerSeralizer(obj.answers.all(), many=True).data
    

class FinishTestSerializer(serializers.Serializer):
    points = serializers.CharField(max_length=100)
    test_id = serializers.IntegerField()


