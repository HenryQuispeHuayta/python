from cgitb import text
from email import message
from mailbox import Message
import tkinter
from tkinter import filedialog
from tkinter import colorchooser
from tkinter.tix import TList, Tree

window = tkinter.Tk()
# print(type(window))

# import pprint
# pprint.pprint(dir(window))

# labalSaludo = tkinter.Label(window, text='Hola', bg='yellow', fg='blue')
# # labalSaludo.pack(ipadx=50, ipady= 50, fill='x',fill='x')
# labalSaludo.pack(ipadx=30, ipady= 30, side='left')

# labelAdios = tkinter.Label(window, text='Adios', bg='red', fg='white')
# # labelAdios.pack(fill='both',fill='x')
# labelAdios.pack(ipadx=30, ipady=30, side='right')


# labal1 = tkinter.Label(window, text='label1', bg='yellow', fg='blue')
# labal1.pack(ipadx=45, ipady=15, fill='x')

# labal2 = tkinter.Label(window, text='label2', bg='purple', fg='white')
# labal2.pack(ipadx=45, ipady=15, fill='x')

# labal3 = tkinter.Label(window, text='label3', bg='blue', fg='white')
# labal3.pack(ipadx=45, ipady=15, fill='x')

# labal4 = tkinter.Label(window, text='label4', bg='red', fg='white')
# labal4.pack(ipadx=15, ipady=15, side='left')

# labal5 = tkinter.Label(window, text='label5', bg='yellow', fg='black')
# labal5.pack(ipadx=15, ipady=15, side='left')

# labal6 = tkinter.Label(window, text='label6', bg='green', fg='black')
# labal6.pack(ipadx=15, ipady=15, side='right')

from tkinter import Tk, ttk

# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=3)

# # Usuario
# # Etiqueta Usuario
# usernameLabel = ttk.Label(window, text='Username: ')
# usernameLabel.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# # Campo Usuario
# usernameEntry = ttk.Entry(window)
# usernameEntry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# # Password
# # Etiqueta Password
# passwordLabel = ttk.Label(window, text='Password: ')
# passwordLabel.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# # Campo Password
# passwordEntry = ttk.Entry(window, show='*')
# passwordEntry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# # Boton
# loginButton = ttk.Button(window, text='Login')
# loginButton.grid(column=1,row=3, sticky=tkinter.E, padx=5, pady=5)

# # Boton 2
# loginButton = ttk.Button(window, text='row 1')
# loginButton.grid(column=1,row=1, sticky=tkinter.W, padx=5, pady=5)

# # Boton 3
# loginButton = ttk.Button(window, text='row 2')
# loginButton.grid(column=1,row=2, sticky=tkinter.W, padx=5, pady=5)



# import random
# colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

# for x in range(0,10):
#   color = random.randint(0, len(colors)-1)
#   color2 = random.randint(0, len(colors)-1)
#   ancho = random.randint(0, 50)
#   alto = random.randint(0, 100)
#   label = tkinter.Label(window, text='Etiqueta', bg=colors[color], fg= colors[color2])
#   label.place(x=random.randint(0,100),y=random.randint(0,100))



# label1 = tkinter.Label(window, text='Posicionamiento absoluto', bg='blue', fg='white')
# label1.place(x=10,y=50)

# label2 = tkinter.Label(window, text='Otro mas', bg='red', fg='yellow')
# # label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')
# label2.place(x=25, y=30)



window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
# listaItems = tkinter.StringVar(value=lista)
# listbox = tkinter.Listbox(window, height=100, listvariable=listaItems)
# listbox.grid(column=0, row=0, sticky=tkinter.W)



# frame = ttk.Frame(window)

# label = ttk.Label(frame, text='hola')
# label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

# frame.grid(column=0, row=0, sticky=tkinter.W)
# frame['relief'] = 'sunken'


# seleccionado = tkinter.StringVar()
# r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
# r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
# r3 = ttk.Radiobutton(window, text='Quiza', value='3', variable=seleccionado)

# r1.grid(column=0, row=1, padx=5, pady=5)
# r2.grid(column=0, row=2, padx=5, pady=5)
# r3.grid(column=0, row=3, padx=5, pady=5)

# seleccionado2 = tkinter.StringVar()
# rs1 = ttk.Radiobutton(window, text='Si2', value='12', variable=seleccionado2)
# rs1.grid(column=1, row=0, padx=5, pady=5)


# def mifuncion():
#   print('clicado')

# seleccionado = tkinter.StringVar()

# checkbox = ttk.Checkbutton(window, text='acepto las condiciones', variable=seleccionado, command=mifuncion)
# checkbox.grid(column=0, row=0)



# def salir(event):
#   print('Adios')
#   window.quit()

# def saludar(event):
#   print('Han hecho click en saludar')

# def saludarDobleClick(event):
#   print('Han hecho click en saludar Doble')


# boton = tkinter.Button(window, text='Haz Click')
# boton.pack()
# boton.bind('<Button-1>', saludar)
# boton.bind('<Double-1>', saludarDobleClick)

# botonSalir = tkinter.Button(window, text='Haz Click')
# botonSalir.pack()
# botonSalir.bind('<Button-1>', salir)



# def motion(event):
#   print(f'Mouse position: ({event.x} {event.y})')
#   return

# master = Tk()
# texto = 'Demo de texto en un widget msg para ver el movimiento del raton'
# msg = Message(master, text=texto)
# msg.config(bg='ligthgreen', font=('time', 24, 'italic'))
# msg.bind('<Motion>', motion)
# msg.pack()



# from tkinter import filedialog
# filename = filedialog.askopenfilename()
filename = colorchooser.askcolor(initialcolor='#ffffff')


window.mainloop()