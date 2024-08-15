from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Rule(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Эреже'
        verbose_name_plural = 'Эрежелер'


class RuleCard(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Эреженин карточкасы'
        verbose_name_plural = 'Эреженин карточкалары'