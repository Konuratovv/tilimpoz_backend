from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from . import models
from . import serializers

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TestCategoryListAPIView(generics.ListAPIView):
    queryset = models.TestCategory.objects.all()
    serializer_class = serializers.TestCategorySerializer


class TestListAPIView(generics.ListAPIView):
    queryset = models.Test.objects.all().select_related('article')
    serializer_class = serializers.TestListSerializer


class QuestionsListAPIView(generics.ListAPIView):
    serializer_class = serializers.QuestionsListSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'test_id', 
                openapi.IN_BODY, 
                description="id Теста", 
                type=openapi.TYPE_STRING
            )
        ],
        responses={200: 'OK'}
    )
    def get_queryset(self):
        test_id = self.request.data.get('test_id')
        return models.Question.objects.filter(id=test_id).select_related('test')
    
            




