from django.db import models

class Book(models.Model):
    photo = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
