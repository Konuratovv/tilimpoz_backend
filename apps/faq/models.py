from django.db import models


# Create your models here.

class Faq(models.Model):
    question = models.TextField(verbose_name='Суроо')
    answer = models.TextField(verbose_name='Жооп')

    def __str__(self):
        return (
            f'Question: {self.question}'
            f'\nAnswer: {self.answer}'
        )

    class Meta:
        verbose_name = 'Эн коп берилген суроо'
        verbose_name_plural = 'Эн коп берилген суроолор'

