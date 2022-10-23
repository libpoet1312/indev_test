from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=1024)

    def __str__(self):
        return self.title
