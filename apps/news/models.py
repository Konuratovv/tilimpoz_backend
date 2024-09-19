from django.db import models

from apps.categories.models import Category

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аты')
    photo = models.ImageField(upload_to='news/', verbose_name='Сурот')
    date = models.DateField(auto_now_add=True, verbose_name='Тузулгон убактысы')
    description = models.TextField(verbose_name='Баяндалышы')
    article = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news', verbose_name='Макаланын категориясы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Жанылык'
        verbose_name_plural = 'Жанылыктар'
