from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
            manual_parameters=[
                openapi.Parameter(
                    'question',
                    openapi.IN_FORM,
                    description='Текст для вопроса',
                    type=openapi.TYPE_STRING
                ),
                openapi.Parameter(
                    'image',
                    openapi.IN_FORM,
                    description='А это для загрузки картинки с вопросом',
                    type=openapi.TYPE_FILE,
                )
            ],
            responses={201: "CREATED"},
            operation_description='Сначала вставьте access token в форму Authorize сверху'
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.create(
            question=serializer.validated_data['question'],
            image=serializer.validated_data['image'],
            nickname=self.request.user,
        )
        question.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)