from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path

urlpatterns = [
    path('', BookViewSet.as_view(), name='book')
]