from django.urls import path

from .views import main_page_articles, SearchAPIView, SearchHistoryListAPIView

urlpatterns = [
    path('main-page/', main_page_articles, name='main-page-articles'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('search-history/', SearchHistoryListAPIView.as_view(), name='search-history'),
]