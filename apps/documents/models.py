from django.db import models

class Document(models.Model):
    photo = models.ImageField(upload_to='documents/')
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.file.name