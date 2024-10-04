from django.urls import path

from .views import MainPageAPIVIew, SearchAPIView, SearchHistoryListAPIView, DeleteSearchHistoryAPIView

urlpatterns = [
    path('main-page/', MainPageAPIVIew.as_view(), name='main-page-articles'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('search-history/', SearchHistoryListAPIView.as_view(), name='search-history'),
    path('search-history/<int:query_id>', DeleteSearchHistoryAPIView.as_view(), name='delete-search-history'),
]