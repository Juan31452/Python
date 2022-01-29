import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.config(width=300, height=200)
# Crear caja de texto.
entry = ttk.Entry(ventana)
# Posicionarla en la ventana.
entry.place(x=50, y=50)
ventana.mainloop()