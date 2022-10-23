import time 

def calcular():
  res = ''
  tiempo = time.localtime()
  res = 'Faltan ' + (18 -   tiempo[3]).__str__() + ':' + (59 -   tiempo[4]).__str__() + ' para volver a casa'
  if(tiempo[3] >= 19):
    res = 'Es hora de volver a casa'
  return res

print(calcular())

