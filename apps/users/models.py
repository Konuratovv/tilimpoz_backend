from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from .user_manager import UserManager


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True, verbose_name='Почтасы')
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150, verbose_name='Никнейм')
    points = models.IntegerField(default=0, verbose_name='Баллдар')
    code = models.CharField(max_length=9, blank=True, null=True, verbose_name='Почтаны аныктоо учун убактылуу коду')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = 'Колдонуучу'
        verbose_name_plural = 'Колдонуучулар'

    def save(self, **kwargs):
        self.password = make_password(self.password)
        return super().save(**kwargs)
