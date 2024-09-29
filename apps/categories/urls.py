from django.urls import path

from .views import MainPageAPIVIew, SearchAPIView, SearchHistoryListAPIView

urlpatterns = [
    path('main-page/', MainPageAPIVIew.as_view(), name='main-page-articles'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('search-history/', SearchHistoryListAPIView.as_view(), name='search-history'),
]