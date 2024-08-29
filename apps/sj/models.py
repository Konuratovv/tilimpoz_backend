from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.categories.models import Category

# Create your models here.

class SabattuuModel(models.Model):
    image = models.ImageField(upload_to='sj/', verbose_name='Сурот')
    title = models.CharField(max_length=300, verbose_name='Аты')
    description = CKEditor5Field(verbose_name='Текст')
    photo2 = models.ImageField(upload_to='sj/', verbose_name='Сурот 2')
    description2 = CKEditor5Field(verbose_name='Текст 2')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sj', verbose_name='Категориясы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')

    def __str__(self) -> str:
        return 'Сабаттуу жообтор'
    
    class Meta:
        verbose_name = 'Сабаттуу жообтор'
        verbose_name_plural = 'Сабаттуу жообтор'