from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleViewSet.as_view({'get': 'list'}), name='article-list-create'),
]