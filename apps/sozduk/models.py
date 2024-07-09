from django.db import models

class Sozduk(models.Model):
    category = models.CharField(max_length=100)
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sozduk_images/', null=True, blank=True)

    def __str__(self):
        return self.word

