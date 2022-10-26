from functools import reduce

def main():
  res = calcular([1,2,3,4,5,6,7,8,9,10])
  print(res)

def calcular(lista):
  lista2 = filter(lambda x: x%2, lista)
  res = reduce(lambda a,b: a+b, lista2)
  return res

if __name__ == '__main__':
  main()