from django.db import models
from apps.categories.models import Category


class SozdukCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Аты')
    image = models.ImageField(upload_to='sozduk/category/', verbose_name='Сурот')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sozduk', verbose_name='Категориясы')

    def __str__(self) -> str:
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = 'Создуктун категориясы'
        verbose_name_plural = 'Создуктун категориялары'


class Sozduk(models.Model):
    word = models.CharField(max_length=200, verbose_name='Соз')
    translation = models.CharField(max_length=200, verbose_name='Котормосу')
    image = models.ImageField(upload_to='sozduk/sozdor/', null=True, blank=True, verbose_name='Сурот')
    category = models.ForeignKey(SozdukCategory, on_delete=models.CASCADE, related_name='soz', verbose_name='Категориясы')

    def __str__(self):
        return self.word
    

    class Meta:
        verbose_name = 'Соз'
        verbose_name_plural = 'Создор'

