from django.db.models import Q

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

from .models import SearchHistory


def get_random_articles(request):
    tilibizde = Tilibizde.objects.order_by('?')[:2]
    etymology = Etymology.objects.order_by('?')[:2]
    sozduk = SozdukCategory.objects.order_by('?')[:2]
    sj = SabattuuModel.objects.order_by('?')[:2]
    books = Book.objects.order_by('?')[:2]
    test = Test.objects.order_by('?')[:2]

    serializer_data = []

    serializer_data += TilibizdeCardSerializer(tilibizde, many=True).data
    serializer_data += EtymologySerializer(etymology, many=True).data
    serializer_data += SozdukSerializer(sozduk, many=True).data
    serializer_data += SabattuuJoobtorListSerializer(sj, many=True).data
    serializer_data += BookSerializer(books, many=True).data
    serializer_data += TestListSerializer(test, many=True).data
    
    for item in serializer_data:
        if 'photo' in item:
            item['photo'] = request.build_absolute_uri(item['photo'])
            
        if 'file' in item:
            item['file'] = request.build_absolute_uri(item['file'])
            
    return serializer_data
    
def search(current_user, query):
    serializer_data = []
    tilibizde = Tilibizde.objects.filter(Q(title__icontains=query) | 
                                        Q(description__icontains=query) | 
                                        Q(description2__icontains=query) | 
                                        Q(category__title=query)).select_related(
                                            'category'
                                        )
    tilibizde_serializer = TilibizdeCardSerializer(tilibizde, many=True)
    etymology = Etymology.objects.filter(Q(title__icontains=query) | 
                                        Q(description__icontains=query) | 
                                        Q(description2__icontains=query) | 
                                        Q(category__title=query)).select_related(
                                            'category'
                                        )
    etymology_serializer = EtymologySerializer(etymology, many=True)
    sabattuu = SabattuuModel.objects.filter(Q(title__icontains=query) | 
                                            Q(description__icontains=query) | 
                                            Q(description2__icontains=query) | 
                                            Q(category__title=query)).select_related(
                                                'category'
                                            )
    sabattuu_serializer = SabattuuJoobtorListSerializer(sabattuu, many=True)
    sozduk = SozdukCategory.objects.filter(Q(title__icontains=query) | 
                                        Q(category__title=query)).select_related(
                                            'category'
                                        )
    sozduk_serializer = SozdukSerializer(sozduk, many=True)
    book = Book.objects.filter(Q(title__icontains=query) | 
                            Q(description__icontains=query) | 
                            Q(book_category__title=query) |
                            Q(category__title=query)).select_related(
                                'category'
                            )
    book_serializer = BookSerializer(book, many=True)
    test = Test.objects.filter(Q(title__icontains=query) | 
                            Q(category__title=query)).select_related(
                                'category'
                            )
    test_serializer = TestListSerializer(test, many=True)

    serializer_data += tilibizde_serializer.data
    serializer_data += etymology_serializer.data
    serializer_data += sabattuu_serializer.data
    serializer_data += sozduk_serializer.data
    serializer_data += book_serializer.data
    serializer_data += test_serializer.data
    
    if not current_user.is_anonymous and query is not None:
        search_history = SearchHistory.objects.create(
            query=query,
            users=current_user
        )
        search_history.save()
        
    return serializer_data
