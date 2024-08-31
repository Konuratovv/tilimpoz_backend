from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.tilibizde.models import Tilibizde
from apps.etymology.models import Etymology
from apps.sozduk.models import SozdukCategory
from apps.sj.models import SabattuuModel
from apps.books.models import Book
from apps.tilibizde.serializers import TilibizdeCardSerializer
from apps.etymology.serializers import EtymologySerializer
from apps.sozduk.serializers import SozdukSerializer
from apps.sj.serializers import SabattuuJoobtorListSerializer
from apps.books.serializers import BookSerializer




@api_view(['GET'])
def main_page_articles(request):
    tilibizde = Tilibizde.objects.order_by('?')[:3]
    etymology = Etymology.objects.order_by('?')[:3]
    sozduk = SozdukCategory.objects.order_by('?')[:3]
    sj = SabattuuModel.objects.order_by('?')[:3]
    books = Book.objects.order_by('?')[:3]

    serializer_data = []

    serializer_data += TilibizdeCardSerializer(tilibizde, many=True).data
    serializer_data += EtymologySerializer(etymology, many=True).data
    serializer_data += SozdukSerializer(sozduk, many=True).data
    serializer_data += SabattuuJoobtorListSerializer(sj, many=True).data
    serializer_data += BookSerializer(books, many=True).data
    return Response(serializer_data, status=status.HTTP_200_OK)

    
