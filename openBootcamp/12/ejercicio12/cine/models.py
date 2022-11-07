from django.urls import reverse
from django.db import models

# Create your models here.

class Genero(models.Model):
  name = models.CharField(max_length=64, help_text='Pon el nombre del genero')
  
  def __str__(self):
    return self.name

class Pelicula(models.Model):
  titulo = models.CharField(max_length=32)
  director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
  descripcion = models.TextField(max_length=200, help_text='Descripcion de la pelicula')
  genero = models.ManyToManyField(Genero)
  
  def __str__(self):
    return self.titulo
  
  def get_absolute_url(self):
      return reverse("pelicula_detail", args=[str(self.id)])
  

class Director(models.Model):
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  
  def get_absolute_url(self):
    return reverse("director_detail", args=[str(self.id)])
    
  def __str__(self):
    return '%s, %s' % (self.lastName, self.firstName)
  