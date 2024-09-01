from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCategoryListApiView, BookDetailedAPIView
from django.urls import path

urlpatterns = [
    path('', BookViewSet.as_view(), name='book'),
    path('<int:pk>/', BookDetailedAPIView.as_view(), name='book-detailed'),
    path('categories/', BookCategoryListApiView.as_view(), name='book-categories'),
]