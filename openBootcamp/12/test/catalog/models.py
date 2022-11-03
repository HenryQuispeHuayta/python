from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Genre(models.Model):
  name = models.CharField(max_length=64, help_text='Pon el nombre del genero')
  
  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=32)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
