from django.db import models

from categories.models import Category

EASY_STR = 'Easy'
MEDIUM_STR = 'Medium'
DIFFICULT_STR = 'Difficult'

DIFFICULTY_CHOICES = (
    ('0', EASY_STR),
    ('1', MEDIUM_STR),
    ('2', DIFFICULT_STR)
)


class Question(models.Model):
    question = models.TextField(max_length=1024)

    difficulty = models.CharField(max_length=1,
                                  choices=DIFFICULTY_CHOICES,
                                  default=0
                                  )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
