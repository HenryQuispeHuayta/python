from curses import init_pair
import sqlite3
def main():
  crear()
  n = int(input('Ingresar la cantidad de usuarios(8 minimo): '))
  for i in range(n):
    nombre = input('Ingresar nombre: ')
    apellido = input('Ingresar apellido: ')
    add(nombre, apellido)
  
  nombreBuscar = input('Nombre a buscar: ')
  buscar(nombreBuscar)


def crear():
  con = sqlite3.connect('ejercicio1.db')
  cursor = con.cursor()
  
  query = 'create table Alumnos(id integer primary key autoincrement, nombre text not null, apellido text)'
  cursor.execute(query)
  
  cursor.close()
  con.close()
  
def add(nombre, apellido):
  con = sqlite3.connect('ejercicio1.db')
  cursor = con.cursor()
  
  query = '''insert into Alumnos(nombre, apellido) values(?, ?)'''
  cursor.execute(query, (nombre, apellido))
  con.commit()
  
  cursor.close()
  con.close()
  
def buscar(nombre):
  con = sqlite3.connect('ejercicio1.db')
  cursor = con.cursor()
  
  query = f'select * from Alumnos where nombre="{nombre}"'
  rows = cursor.execute(query)
  for row in rows:
    print(row)
  
  cursor.close()
  con.close()
  
  
if __name__=='__main__':
  main()