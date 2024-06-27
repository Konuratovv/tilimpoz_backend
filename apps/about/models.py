from django.db import models

class About(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='about/')

    def __str__(self):
        return "About"
