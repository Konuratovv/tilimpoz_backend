from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PartnersListAPIView.as_view(), name='partners')
]
