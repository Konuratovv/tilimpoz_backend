from django.urls import path
from . import views

urlpatterns = [
    path('', views.RuleListCreateAPIView.as_view(), name='rule-list-create'),
]