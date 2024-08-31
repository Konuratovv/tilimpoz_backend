from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCategoryListApiView
from django.urls import path

urlpatterns = [
    path('', BookViewSet.as_view(), name='book'),
    path('categories/', BookCategoryListApiView.as_view(), name='book-categories'),
]