from django.db import models
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категориянын аты')

    def __str__(self) -> str:
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = 'Китептин категориясы'
        verbose_name_plural = 'Китептин категориялары'


class Book(models.Model):
    photo = models.ImageField(upload_to='books/', verbose_name='Сурот')
    title = models.CharField(max_length=200, verbose_name='Аты')
    description = models.TextField(verbose_name='Баяндалышы')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book', verbose_name='Категория')
    file = models.FileField(upload_to='books/', verbose_name='Китептин файлы', validators=(FileExtensionValidator(('pdf', )), ))
    year = models.CharField(max_length=4, help_text='Мисалы: 2014', verbose_name='Чыгарылган жылы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Китеп'
        verbose_name_plural = 'Китептер'
