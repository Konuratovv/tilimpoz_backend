from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentListCreateAPIView.as_view(), name='document-list-create'),
]