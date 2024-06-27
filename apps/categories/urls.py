# categories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
]