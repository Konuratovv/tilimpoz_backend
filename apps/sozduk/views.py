from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Sozduk, SozdukCategory
from .serializers import SozdukSerializer, SozdorSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class SozdukCategoryListAPIView(generics.ListAPIView):
    queryset = SozdukCategory.objects.all()
    serializer_class = SozdukSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class SozdorListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Sozduk.objects.all()
    serializer_class = SozdorSerializer

    
    def get(self, request, *args, **kwargs):
        category_id = self.kwargs['category_id']
        queryset = self.get_queryset().filter(category__id=category_id)
        serializer = SozdorSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


