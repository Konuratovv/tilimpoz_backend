from django.contrib import admin
from django.urls import path, include
from .views import register, login, top_users, verification, reset_password

urlpatterns = [
    path('register/', register.RegisterAPIView.as_view(), name='register'),
    path('login/', login.LoginAPIView.as_view(), name='login'),
    path('top-users/', top_users.TopUsersAPIView.as_view(), name='top-users'),
    path('verify-email/', verification.VerifyEmailAPIView.as_view(), name='verify-user'),
    path('send-reset-code/', reset_password.SendResetCodeAPIView.as_view(), name='send-reset-code'),
    path('check-reset-code/', reset_password.CheckResetCodeAPIView.as_view(), name='check-reset-code'),
    path('reset-password/', reset_password.ResetPasswordAPIView.as_view(), name='reset-password')
]
