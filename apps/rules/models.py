from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from apps.users.models import CustomUser


class Rule(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аты')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rule', verbose_name='Автор')
    description = CKEditor5Field(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон датасы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Эреже'
        verbose_name_plural = 'Эрежелер'