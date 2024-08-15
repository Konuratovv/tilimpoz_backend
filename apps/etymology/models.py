from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Etymology(models.Model):
    photo = models.ImageField(upload_to='etymology/', verbose_name='Сурот')
    title = models.CharField(max_length=255, verbose_name='Аты')
    description = CKEditor5Field(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Этимология'
        verbose_name_plural = 'Этимология'