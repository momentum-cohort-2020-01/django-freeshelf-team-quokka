from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return f"Book title: {self.title} author: {self.author} description: {self.description} "

