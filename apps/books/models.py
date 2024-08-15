from django.db import models

class Book(models.Model):
    photo = models.ImageField(upload_to='books/', verbose_name='Сурот')
    title = models.CharField(max_length=200, verbose_name='Аты')
    description = models.TextField(verbose_name='Баяндалышы')
    category = models.CharField(max_length=100, verbose_name='Категориясы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Китепкана'
        verbose_name_plural = 'Китепкана'
