from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аты')
    category = models.CharField(max_length=255, default='General', verbose_name='Категория')
    date = models.DateField(default=timezone.now, verbose_name='Тузулгон датасы')
    photo = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name='Сурот')
    description = models.TextField(verbose_name='Баяндалышы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Макала'
        verbose_name_plural = 'Макалалар'

