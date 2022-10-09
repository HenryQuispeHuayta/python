from mailbox import NoSuchMailboxError


class Alumno:
  nombre = None
  nota = None
  
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    
  def aprobo(self):
    if(self.nota > 50):
      print(self.nombre, 'aprobo con ', self.nota)
    else:
      print(self.nombre, 'reprobo con ', self.nota)
      
alumno = Alumno('Henry', 51)
alumno.aprobo()