from django.shortcuts import render
from .serializers import TestCategorySerializer, TestSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import TestCategory, Test
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CategoryListAPIView(ListAPIView):
    queryset = TestCategory.objects.all()
    serializer_class = TestCategorySerializer
    permission_classes = (AllowAny, )


class TestByCategoryListAPIView(APIView):
    def get(self, request):
        category_id = self.request.get('category_id')
        queryset = Test.objects.filter(category__id=category_id)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





