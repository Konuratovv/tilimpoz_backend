from django.db import models

class Etymology(models.Model):
    photo = models.ImageField(upload_to='etymology/')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title