from django.db import models


# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='Телефон номери')
    email = models.EmailField(verbose_name='Уюлдук почтасы')
    address = models.TextField(verbose_name='Дарек')

    def __str__(self):
        return self.phone_number
    

    class Meta:
        verbose_name = 'Байланыш'
        verbose_name_plural = 'Байланыштар'


class SocialMedia(models.Model):
    link = models.CharField(max_length=350, verbose_name='Шилтеме')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='social_media', verbose_name='Байланыштары')

    def __str__(self):
        return self.link
    

    class Meta:
        verbose_name = 'Социалдык тармак'
        verbose_name_plural = 'Социалдык тармактар'