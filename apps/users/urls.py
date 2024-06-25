from django.contrib import admin
from django.urls import path, include
from .views import register, login

urlpatterns = [
    path('register/', register.RegisterAPIView.as_view(), name='register'),
    path('login/', login.LoginAPIView.as_view(), name='login'),
]
