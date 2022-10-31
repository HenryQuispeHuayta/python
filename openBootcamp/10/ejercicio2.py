import tkinter as tk
from tkinter import ttk

window = tk.Tk()

seleccionado1 = tk.StringVar()
seleccionado2 = tk.StringVar()
seleccionado3 = tk.StringVar()

cb1 = ttk.Checkbutton(window, text='checkbox 1', variable=seleccionado1)
cb2 = ttk.Checkbutton(window, text='checkbox 2', variable=seleccionado2)
cb3 = ttk.Checkbutton(window, text='checkbox 3', variable=seleccionado3)

cb1.grid(row=0, column=0)
cb2.grid(row=1, column=0)
cb3.grid(row=2, column=0)

texto = tk.Label(text='Estos son checkbox')
texto.grid(row=3,column=0)

window.mainloop()