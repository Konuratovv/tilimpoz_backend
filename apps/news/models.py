from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='news/')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
