from django.db import models

class Category(models.Model):
    photo = models.ImageField(upload_to='categories/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
