from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING, blank=True, null=True)
    

    def __str__ (self):
        return f"Book title: {self.title} author: {self.author} description: {self.description} "

class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)  