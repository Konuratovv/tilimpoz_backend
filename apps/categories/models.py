from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Макаланын категориясы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Макаланын категориясы'
        verbose_name_plural = 'Макаланын категориялары'
