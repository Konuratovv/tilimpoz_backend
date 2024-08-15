from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='videos/')
    youtube_url = models.URLField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Кормо'
        verbose_name_plural = 'Кормолор'