from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from apps.categories.models import Category

class Etymology(models.Model):
    photo = models.ImageField(upload_to='etymology/', verbose_name='Сурот')
    title = models.CharField(max_length=255, verbose_name='Аты')
    description = models.TextField(verbose_name='Текст')
    photo2 = models.ImageField(upload_to='etymology/', verbose_name='Сурот 2')
    description2 = models.TextField(verbose_name='Текст 2')
    category = models.ForeignKey(Category, related_name='etymology', on_delete=models.CASCADE, verbose_name='Макаланын категориясы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Этимология'
        verbose_name_plural = 'Этимология'