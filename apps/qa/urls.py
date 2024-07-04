from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuestionListAPIView.as_view(), name='question-list'),
    path('create/', views.QuestionCreateAPIView.as_view(), name='question-create'),
]