from django.urls import path

from .views import main_page_articles

urlpatterns = [
    path('main-page/', main_page_articles, name='main-page-articles'),
]