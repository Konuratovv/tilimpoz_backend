from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListCreateAPIView.as_view(), name='article-list-create'),
]