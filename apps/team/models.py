from django.db import models


# Create your models here.

class Team(models.Model):
    image = models.ImageField(upload_to="team_images/")
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name