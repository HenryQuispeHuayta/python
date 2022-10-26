# import _thread
# import time

# def horaActual(nombreThread, tiempoDeEspera):
#   count = 0
#   while count < 5:
#     time.sleep(tiempoDeEspera)
#     count += 1
#     print(f'hilo: {nombreThread} - {time.ctime()}')

# _thread.start_new_thread(horaActual,('threadUno', 1))
# _thread.start_new_thread(horaActual,('threadDos', 2))

# print('He disparado los hilos')


# import logging

# logging.basicConfig(level=logging.INFO)
# logging.debug('Prueba debug')
# logging.info('Arrancando el programa')
# logging.warning('Hace calor')
# logging.error('test')
# logging.critical('adios')


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def mifuncion(x):
#   # if x % 2 == 0:
#   if str(x).startswith('pep'):
#     return True
#   return False

# # resultado = filter(mifuncion,numeros)
# # resultado = filter(lambda x: x%2==0,numeros)

# # resultado = filter(mifuncion,['pepe', 'pepito','juan'])
# resultado = filter(lambda x: str(x).startswith('pep'),['pepe', 'pepito','juan'])

# print(list(resultado))


# from cgitb import reset


# def cuadrado(x):
#   return x * x

# # resultado = map(cuadrado,[1, 2, 3, 4, 5, 6, 7, 8, 9])
# resultado = map(lambda x: x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(list(resultado))


# from functools import reduce

# def suma(a, b):
#   print(f'a={a}, b={b}')
#   return a + b

# resultado = reduce(suma,[1, 2, 3, 4, 5])

# print(resultado)


# cursos = ['Java', 'Python', 'Git']
# asistentes = [15, 20, 4]
# demo = zip(cursos, asistentes)
# print(list(demo))


# listaA = [1==1, 2==2, 3==4]
# # res = any(listaA)
# res = all(listaA)
# print(res)


# a = 5.5
# b = 5.4
# c = 5.6
# print(round(a))
# print(round(b))
# print(round(c))


# print(min(2,3,4,5,9,3,1))
# print(pow(2,3))


# lista = ['z', 'c', 'd', 'a']

# ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
# print(ordenada)


# a = input('Como te llamas?')
# print(f'hola, {a}')

# from getpass import getpass
# user = input('username: ')
# passwd = getpass('password: ')

# print(user, passwd)


secreto = 50
valor = 0
while valor != secreto:
  valor = int(input('Introduce un numero: '))
  
  if valor > secreto:
    print('Muy bajo')
    continue
  
  if valor < secreto:
    print('Muy bajo')
    continue
  
  print('Acertaste!')
