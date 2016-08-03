from django.db import models
from datetime import datetime

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100, default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    author = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    
class Feature(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title