from django.db import models
from apps.users.models import CustomUser as User


# Create your models here.

class Question(models.Model):
    question = models.TextField()
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.TextField()
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer
