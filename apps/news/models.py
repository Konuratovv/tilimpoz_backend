from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аты')
    photo = models.ImageField(upload_to='news/', verbose_name='Сурот')
    date = models.DateField(verbose_name='Тузулгон убактысы')
    description = models.TextField(verbose_name='Баяндалышы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Жанылык'
        verbose_name_plural = 'Жанылыктар'
