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
    queryset = models.Test.objects.all().select_related('category')
    serializer_class = serializers.TestListSerializer


class QuestionsListAPIView(generics.ListAPIView):
    serializer_class = serializers.QuestionsListSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'test_id', 
                openapi.IN_QUERY, 
                description="id Теста", 
                type=openapi.TYPE_STRING
            )
        ],
        responses={200: 'OK'}
    )
    def get_queryset(self):
        test_id = self.request.data.get('test_id')
        return models.Question.objects.filter(id=test_id).select_related('test')
    

class RecieveAndShowPoints(generics.UpdateAPIView):
    serializer_class = serializers.PointSerializer

    def patch(self, request, *args, **kwargs):
        points = self.request.data.get('points')
        user = self.request.user
        if user.is_authenticated():
            user.points = int(points)
            return Response({"points": points}, status=status.HTTP_200_OK)
        else:
            return Response({"points": points}, status=status.HTTP_200_OK)
            




