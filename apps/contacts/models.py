from django.db import models


# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='Телефон номери')
    email = models.EmailField(verbose_name='Уюлдук почтасы')
    address = models.TextField(verbose_name='Дарек')
    insta_link = models.URLField(null=True ,blank=True ,verbose_name='Инстаграм баракчасы')
    tg_link = models.URLField(null=True ,blank=True ,verbose_name='Телеграм')
    whatsapp_link = models.URLField(null=True ,blank=True ,verbose_name='Whatsapp дареги')
    threads_link = models.URLField(null=True ,blank=True ,verbose_name='Threads баракчасы')
    twitter_link = models.URLField(null=True ,blank=True ,verbose_name='Twitter баракчасы')

    def __str__(self):
        return self.phone_number
    

    class Meta:
        verbose_name = 'Байланыш'
        verbose_name_plural = 'Байланыштар'