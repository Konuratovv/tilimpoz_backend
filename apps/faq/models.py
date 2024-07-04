from django.db import models


# Create your models here.

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return (
            f'Question: {self.question}'
            f'\nAnswer: {self.answer}'
        )

    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

