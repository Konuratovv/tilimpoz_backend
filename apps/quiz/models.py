from typing import Iterable
from django.db import models

from apps.categories.models import Category

# Create your models here.

class TestCategory(models.Model):
    title = models.CharField(max_length=350, verbose_name='Категориянын аталышы')


    class Meta:
        verbose_name = 'Тесттин категориясы'
        verbose_name_plural = 'Тесттин категориялары'

    def __str__(self) -> str:
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=350, verbose_name='Тесттин аталышы')
    image = models.ImageField(upload_to='test/', verbose_name='Тесттин суроту')
    article = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='test', verbose_name='Макаланын категориясы')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, verbose_name='Тесттин категориясы')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесттер'

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    question = models.TextField(verbose_name='Тесттин суроосу')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', verbose_name='Тест')

    
    class Meta:
        verbose_name = 'Суроо'
        verbose_name_plural = 'Суроолор'

    def __str__(self) -> str:
        return self.question
    

class Answer(models.Model):
    answer = models.TextField(verbose_name='Жооп')
    is_correct = models.BooleanField(default=False, verbose_name='Туурабы?')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Жооптун суроосу')

    class Meta:
        verbose_name = 'Жооп'
        verbose_name_plural = 'Жооптор'

    def __str__(self) -> str:
        return self.answer

