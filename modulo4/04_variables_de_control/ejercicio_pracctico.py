"""
Ejercicio práctico: formulario_controlado.py
Crea una app que:

Use un StringVar enlazado a un Entry.

Tenga un botón "Mostrar" que imprima en consola el valor actual del StringVar.

Tenga un botón "Borrar" que borre el valor del campo.
"""

#importamos la libreria tkinter
import tkinter as tk

#funcion para mostrar el valor del stringvar
def mostrar():
    print(entrada_var.get())

#funcion para borrar el valor del stringvar
def borrar():
    entrada_var.set("")

ventana = tk.Tk()
ventana.title("Formulario controlado")

# Crear frame contenedor
frame = tk.Frame(ventana,width=400, height=400)
frame.pack(padx=10, pady=10)

#crear stringvar
entrada_var = tk.StringVar()

# Widgets dentro del frame
tk.Label(frame, text="Texto:").grid(row=0, column=0)

entrada = tk.Entry(frame, textvariable=entrada_var)
entrada.grid(row=0, column=1)

tk.Button(frame, text="Mostrar", command=mostrar).grid(row=1, column=0, columnspan=2)
tk.Button(frame, text="Borrar", command=borrar).grid(row=2, column=0, columnspan=2)

ventana.mainloop()