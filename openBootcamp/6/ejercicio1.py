class Vehiculo:
  color = 'blanco'
  ruedas = 4
  puertas = 2
  
class Coche(Vehiculo):
  velocidad = 15
  cilindarada = True
  
coche = Coche()

print('El coche tiene una velocidad de ',coche.velocidad)
print('El coche tiene es cilindrado ',coche.cilindarada)
print('El coche tiene un color de ',coche.color)
print('El coche tiene ',coche.ruedas, ' ruedas')
print('El coche tiene ',coche.puertas, ' puertas')