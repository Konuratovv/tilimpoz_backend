from rest_framework import serializers

from .models import Question
from .models import Answer
from apps.users.models import CustomUser as User


class NicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AnswerSerializer(serializers.ModelSerializer):
    nickname = NicknameSerializer()

    class Meta:
        model = Answer
        fields = ('nickname', 'answer', 'created_at')


class ListQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    nickname = NicknameSerializer()

    class Meta:
        model = Question
        fields = ('nickname', 'question', 'created_at', 'answers')

    def get_answers(self, obj):
        answer = Answer.objects.filter(
            question=obj,
        )
        if answer:
            return AnswerSerializer(answer, many=True).data
        else:
            return []


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'image', )
