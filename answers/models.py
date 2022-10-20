from django.db import models

from questions.models import Question


class Answer(models.Model):
    text = models.TextField(max_length=1024)
    correct = models.BooleanField(default=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
