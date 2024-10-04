from django.contrib import admin
from django.urls import path, include
from .views import register, login, top_users, reset_password, logout

urlpatterns = [
    path('register/', register.RegisterAPIView.as_view(), name='register'),
    path('login/', login.LoginAPIView.as_view(), name='login'),
    path('top-users/', top_users.TopUsersAPIView.as_view(), name='top-users'),
    path('send-reset-code/', reset_password.SendResetCodeAPIView.as_view(), name='send-reset-code'),
    path('check-reset-code/', reset_password.CheckResetCodeAPIView.as_view(), name='check-reset-code'),
    path('reset-password/', reset_password.ResetPasswordAPIView.as_view(), name='reset-password'),
    path('current-user/', login.RetrieveCurrentUserAPIView.as_view(), name='current-user'),
    path('logout/', logout.LogOutAPIView.as_view(), name='logout')
]
