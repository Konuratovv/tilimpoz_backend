from django.db import models
from apps.users.models import CustomUser as User


# Create your models here.

class Question(models.Model):
    question = models.TextField(verbose_name='Суроо')
    nickname = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='questions/', blank=True, null=True, verbose_name='Сурот')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')

    def __str__(self):
        return self.question
    

    class Meta:
        verbose_name = 'Суроо'
        verbose_name_plural = 'Суроолор'


class Answer(models.Model):
    answer = models.TextField(verbose_name='Жооб')
    nickname = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name='Суроосу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')

    def __str__(self):
        return self.answer
    

    class Meta:
        verbose_name = 'Жооб'
        verbose_name_plural = 'Жообтор'
