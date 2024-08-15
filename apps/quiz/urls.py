from django.urls import path, include
from . import views

urlpatterns = [
    path('test-categories/', views.CategoryListAPIView.as_view()),
    path('tests', views.TestByCategoryListAPIView.as_view())
]