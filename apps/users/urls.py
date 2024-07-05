from django.contrib import admin
from django.urls import path, include
from .views import register, login, top_users

urlpatterns = [
    path('register/', register.RegisterAPIView.as_view(), name='register'),
    path('login/', login.LoginAPIView.as_view(), name='login'),
    path('top-users/', top_users.TopUsersAPIView.as_view(), name='top-users'),
]
