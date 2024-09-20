from django.db import models


class Team(models.Model):
    photo = models.ImageField(upload_to="team_images/")
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Командалар'