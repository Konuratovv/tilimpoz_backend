from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import SozdorListAPIView, SozdukCategoryListAPIView

urlpatterns = [
    path('', SozdukCategoryListAPIView.as_view(), name='sozduk-category'),
    path('category/<int:category_id>/sozdor/', SozdorListAPIView.as_view(), name='sozdor')
]