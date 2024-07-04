from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TeamListAPIView.as_view(), name='team-list'),
]
