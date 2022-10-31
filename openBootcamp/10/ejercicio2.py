import tkinter as tk
from tkinter import ttk

window = tk.Tk()

lista = ['elemento 1', 'elemento 2', 'elemento 3', 'elemento 4']

vista = tk.Listbox()
vista.insert(0,*lista)
vista.pack()

texto = tk.Label(text='Esto es una lista')
texto.pack()

window.mainloop()