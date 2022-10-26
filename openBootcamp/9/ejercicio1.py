def main():
  entrada = input('Ingresar paises separados por comas: ')
  res = paises(entrada)
  print(res)

def paises(listaPaises):
  lista = str(listaPaises).split(',')
  res = ','.join(sorted(set(lista))) 
  return res
  
if __name__ == '__main__':
  main()