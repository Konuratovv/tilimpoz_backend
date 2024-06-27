from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='General')
    date = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return self.title

