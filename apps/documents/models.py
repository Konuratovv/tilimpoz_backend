from django.db import models
from apps.categories.models import Category

class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name='Документтин аты')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='document', verbose_name='Категориясы')
    photo = models.ImageField(upload_to='documents/', verbose_name='Сурот')
    file = models.FileField(upload_to='documents/', verbose_name='Файл')

    def __str__(self):
        return self.file.name
    

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документтер'