from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Question
from .serializers import ListQuestionSerializer, CreateQuestionSerializer


# Create your views here.


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [AllowAny]


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = CreateQuestionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.create(
            question=serializer.validated_data['question'],
            nickname=self.request.user.nickname,
        )
        question.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)