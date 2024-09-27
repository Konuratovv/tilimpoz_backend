from rest_framework import serializers

from . import models

from ..categories.serializers import CategorySerializer

class TestCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.TestCategory
        fields = ('id', 'title', )


class TestListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    article = CategorySerializer()

    class Meta:
        model = models.Test
        fields = ('id', 'title', 'photo', 'article', 'questions_count')

    def get_questions_count(self, obj):
        return obj.questions.count()
    
class TestTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Test
        fields = ('id', 'title', )

class AnswerSeralizer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = models.Answer
        fields = ('id', 'answer', 'is_correct', 'points')

    def get_points(self, obj):
        return 1 if obj.is_correct else 0
    

class QuestionsListSerializer(serializers.ModelSerializer):
    test = TestTitleSerializer()
    answers = serializers.SerializerMethodField()
    question_number = serializers.SerializerMethodField()

    class Meta:
        model = models.Question
        fields = ('id', 'question', 'test', 'question_number', 'answers')

    def get_answers(self, obj):
        return AnswerSeralizer(obj.answers.all(), many=True).data
    
    def get_question_number(self, obj):
        request = self.context.get('request')
        if request:
            page_number = request.query_params.get('page', '1')
            return page_number
        return None

class FinishTestSerializer(serializers.Serializer):
    points = serializers.CharField(max_length=100)
    test_id = serializers.IntegerField()


