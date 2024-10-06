from django.db import models

# Create your models here.


class Partner(models.Model):
    photo = models.ImageField(upload_to='partners/', verbose_name='Сурот')
    
    class Meta:
        verbose_name = 'Оноктош'
        verbose_name_plural = 'Оноктоштор'
        
    def __str__(self) -> str:
        return self.photo.url