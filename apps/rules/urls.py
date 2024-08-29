from rest_framework.routers import DefaultRouter
from .views import RuleListAPIView, RuleRetrieveAPIView
from django.urls import path

urlpatterns = [
    path('', RuleListAPIView.as_view(), name='rules'),
    path('<int:pk>', RuleRetrieveAPIView.as_view(), name='rule-by-id')
]
