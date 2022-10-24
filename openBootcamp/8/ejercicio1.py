def main():
  crear('archivo.txt','primer texto')
  add('archivo.txt','segundo texto')

def crear(archivo, datos):
  f = open(archivo,'w')
  f.write(datos+'\n')
  f.close()

def add(archivo, datos):
  f = open(archivo, 'a')
  f.write(datos+'\n')

if __name__ == '__main__':
  main()