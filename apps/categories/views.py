from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .services import search, get_random_articles
from . import serializers
from . import models

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



@api_view(['GET'])
def main_page_articles(request):
    serializer_data = get_random_articles()
    return Response(serializer_data, status=status.HTTP_200_OK)


class SearchAPIView(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'query', 
                openapi.IN_QUERY, 
                description="Поисковый запрос", 
                type=openapi.TYPE_STRING
            )
        ],
        responses={200: 'OK'}
    )
    
    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        query = request.query_params.get('query', None)
        if query is not None:
            serializer_data = search(current_user, query)
            return Response(serializer_data, status=status.HTTP_200_OK)
        else:
            return Response([])
        

class SearchHistoryListAPIView(generics.ListAPIView):
    serializer_class = serializers.SearchHistorySerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return models.SearchHistory.objects.filter(
            users=self.request.user
        )

        


    
