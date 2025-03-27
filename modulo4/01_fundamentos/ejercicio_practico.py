"""
Ejercicio práctico: ventana_basica.py
Crea una aplicación que:

Importe tkinter correctamente.

Cree una ventana con título: "Hola, Tkinter".

La ventana debe tener un tamaño de 400x300 píxeles.
"""

import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola, Tkinter")
ventana.geometry("400x300")
ventana.mainloop()