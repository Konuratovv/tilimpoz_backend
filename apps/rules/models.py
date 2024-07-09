from django.db import models
from django.utils import timezone
class Rule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class RuleCard(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.title