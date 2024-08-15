from django.db import models

class About(models.Model):
    description = models.TextField(verbose_name='Баяндалышы')
    photo = models.ImageField(upload_to='about/', verbose_name='Сурот')

    def __str__(self):
        return "About"
    

    class Meta:
        verbose_name = 'Биз жонундо'
        verbose_name_plural = 'Биз жонундо'
