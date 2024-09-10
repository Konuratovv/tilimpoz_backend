from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.TestCategoryListAPIView.as_view(), name='test-categories'),
    path('tests/', views.TestListAPIView.as_view(), name='tests'),
    path('questions/<int:test_id>', views.QuestionsListAPIView.as_view(), name='questions-by-test-id'),
    path('finish-test/', views.FinishTestAPIView.as_view(), name='finish-view')
]