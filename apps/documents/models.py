from django.db import models

class Document(models.Model):
    photo = models.ImageField(upload_to='documents/', verbose_name='Сурот')
    file = models.FileField(upload_to='documents/', verbose_name='Файл')

    def __str__(self):
        return self.file.name
    

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документтер'