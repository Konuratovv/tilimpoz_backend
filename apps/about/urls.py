# about/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutListCreateAPIView.as_view(), name='about-list-create'),
]