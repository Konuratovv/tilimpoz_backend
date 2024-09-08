from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

from apps.tilibizde.models import Tilibizde
from apps.etymology.models import Etymology
from apps.sozduk.models import SozdukCategory
from apps.sj.models import SabattuuModel
from apps.books.models import Book
from apps.quiz.models import Test
from apps.tilibizde.serializers import TilibizdeCardSerializer
from apps.etymology.serializers import EtymologySerializer
from apps.sozduk.serializers import SozdukSerializer
from apps.sj.serializers import SabattuuJoobtorListSerializer
from apps.books.serializers import BookSerializer
from apps.quiz.serializers import TestListSerializer
from .services import search, get_random_articles

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
        query = request.query_params.get('query', None)
        if query is not None:
            serializer_data = search(query)
            return Response(serializer_data, status=status.HTTP_200_OK)
        else:
            return Response([])



        


    
