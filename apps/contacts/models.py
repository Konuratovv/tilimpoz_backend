from django.db import models


# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.phone_number


class SocialMedia(models.Model):
    link = models.CharField(max_length=350)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='social_media')

    def __str__(self):
        return self.link