import getpass
import sqlite3

def main():
  username = input('Nombre de usuario: ')
  passwword = getpass.getpass('Contraseña: ')
  
  if verificarCredenciales(username, passwword):
    print('Login correcto')
  else:
    print('Login incorrecto')

def verificarCredenciales(username, password):
  con = sqlite3.connect('miaplicacion.db')
  cursor = con.cursor()
  query = f'select id from users where username="{username}" and password="{password}"'
  print('Query a ejecutar: ', query)
  
  rows = cursor.execute(query)
  data = rows.fetchone()
  print('data es ', type(data))
  
  cursor.close()
  con.close()
  
  if data == None:
    return False
  return True

if __name__ == '__main__':
  main()
  
# con = sqlite3.connect('miaplicacion.db')
# cursor = con.cursor()

# rows = cursor.execute('select * from users where username="vroman"')
# for row in rows:
#   print(row)

# cursor.close()
# con.close()