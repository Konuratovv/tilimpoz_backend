from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Tilibizde(models.Model):
    photo = models.ImageField(upload_to='tilibizde/')
    title = models.CharField(max_length=200)
    description = CKEditor5Field()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Тилибизде'
        verbose_name_plural = 'Тилибизде'
