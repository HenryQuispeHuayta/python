import tkinter as tk
from tkinter import ttk

window = tk.Tk()

seleccionado = tk.StringVar()

def seleccionar():
  print(seleccionado.get())

r1 = ttk.Radiobutton(window, text='Uno', value='Uno', variable=seleccionado, command=seleccionar)
r2 = ttk.Radiobutton(window, text='Dos', value='Dos', variable=seleccionado, command=seleccionar)
r3 = ttk.Radiobutton(window, text='Tres', value='Tres', variable=seleccionado, command=seleccionar)

r1.grid(row=0, column=0, padx=30, pady=5)
r2.grid(row=1, column=0, padx=30, pady=5)
r3.grid(row=2, column=0, padx=30, pady=5)

def reiniciar(event):
  seleccionado.set(None)

boton = tk.Button(window, text='Reiniciar')
boton.bind('<Button-1>', reiniciar)
boton.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()