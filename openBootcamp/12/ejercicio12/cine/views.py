from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
  numPeliculas = Pelicula.objects.all().count()
  numDirectores = Director.objects.all().count()
  
  return render(
    request,
    'index.html',
    context={
      'numPeliculas' : numPeliculas,
      'numDirectores' : numDirectores
    }
  )