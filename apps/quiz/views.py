from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from . import models
from . import serializers

from .filters import TestFilter
from .services import TestService
from .pagination import CustomPageNumberPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django_filters import rest_framework as filters

class TestCategoryListAPIView(generics.ListAPIView):
    queryset = models.TestCategory.objects.all()
    serializer_class = serializers.TestCategorySerializer
    
    def get(self, request, *args, **kwargs):
        serialized_data = []
        serialized_data.append({'id': 0, 'title': 'Бардыгы'})
        serialized_data += self.get_serializer(self.get_queryset(), many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)        


class TestListAPIView(generics.ListAPIView):
    queryset = models.Test.objects.all().select_related('article')
    serializer_class = serializers.TestListSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = TestFilter


class QuestionsListAPIView(generics.ListAPIView):
    serializer_class = serializers.QuestionsListSerializer
    pagination_class = CustomPageNumberPagination
    queryset = models.Question.objects.all()
    lookup_field = 'test_id'

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return models.Question.objects.filter(test_id=test_id).select_related('test')
    

class FinishTestAPIView(APIView):

    @swagger_auto_schema(
            operation_description= """Нужно ввести id теста который он прошел и вычисленные вами баллы которые он набрал, надеюсь вы так сможете). 
            Я сделал так если пользователь проходит этот тест повторно то баллы ему не зачисляются а только выводятся""",
            request_body=serializers.FinishTestSerializer,
            responses={200: 'Points calculated successfully'}
    )
    def patch(self, request, *args, **kwargs):
        serializer = serializers.FinishTestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        test_id = serializer.validated_data['test_id']
        points = serializer.validated_data['points']
        test = models.Test.objects.filter(id=test_id).first()
        user = self.request.user

        message = TestService.finish_test(user, points, test)
        
        if 'photo' in message:
            message['photo'] = self.request.build_absolute_uri(message['photo'])
        
        return Response(message, status=status.HTTP_200_OK)




    
            




