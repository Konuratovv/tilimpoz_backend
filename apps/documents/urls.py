from rest_framework.routers import DefaultRouter
from .views import DocumentListAPIView

from django.urls import path


urlpatterns = [
    path('', DocumentListAPIView.as_view(), name='documents')
]