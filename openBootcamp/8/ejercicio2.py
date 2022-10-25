import pickle

def main():
  f = open('archivo.bin','wb')
  v1 = Vehiculo('toyota', 4, '123qwe')
  pickle.dump(v1,f)
  f.close()
  
  f = open('archivo.bin','rb')
  vehiculo = pickle.load(f)
  f.close()
  print(vehiculo.marca)

class Vehiculo:
  marca = ''
  puertas = 0
  placa = ''
  
  def __init__(self, marca, puertas, placa):
    self.marca = marca
    self.puertas = puertas
    self.placa = placa
    
if __name__ == '__main__':
  main()