# def main():
#   usuarios = listarUsuarios()
#   # print(usuarios)
#   for usuario in usuarios:
#     print(f'Usuario: {usuario}')

# def listarUsuarios():
#   f = open('/etc/passwd','r')
#   datos = f.readlines()
#   f.close()

#   resultado = []
#   for linea in datos:
#     if linea[0] == '#':
#       continue
#     if linea[0] == '_':
#       continue

#     partes = linea.split(':')
#     resultado.append(partes[0])

#   return resultado

# if __name__ == '__main__':
#   main()


# def escribe(fichero, datos):
#   f = open(fichero, 'w')
#   for linea in datos:
#     if not linea.endswith('\n'):
#       linea += '\n'
#     f.write(linea)
#   f.close()

# lista = ['una linea',
#          'dos lineas',
#          'tres lineas']
# escribe('mifichero.txt', lista)


import pickle

class Juguete:
  nombre = ""
  precio = 0.0
  
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self. precio = precio
    
  def getNombre(self):
    return self.nombre
  
  
# j1 = Juguete("Potato", 10.5)
# f = open('datos.bin','wb')

# pickle.dump(j1,f)
# f.close()

f = open('datos.bin','rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre())