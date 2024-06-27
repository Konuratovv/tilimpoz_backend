from django.db import models

class Tilibizde(models.Model):
    photo = models.ImageField(upload_to='tilibizde/')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
