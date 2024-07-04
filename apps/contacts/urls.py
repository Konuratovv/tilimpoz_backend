from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ContactsListAPIView.as_view(), name='contacts-list'),
]