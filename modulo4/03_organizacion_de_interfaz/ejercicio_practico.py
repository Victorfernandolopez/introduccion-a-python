"""
Ejercicio práctico: formulario_grid.py
Crea un formulario con grid() que tenga:

Etiqueta "Usuario" + campo de entrada (fila 0).

Etiqueta "Contraseña" + campo de entrada (fila 1).

Botón "Ingresar" (fila 2, columna 0, columnspan=2).

Al presionar el botón, mostrar "Bienvenido, [usuario]" en una etiqueta nueva.

🧠 Todo debe estar dentro de un Frame.
"""

import tkinter as tk

def bienvenido():
    nombre = usuario_entrada.get()
    etiqueta_usuario.config(text=f"Bienvenido, {nombre}")

ventana = tk.Tk()
ventana.title("Formulario con Grid")

# Crear frame contenedor
frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

# Widgets dentro del frame
tk.Label(frame, text="Usuario:").grid(row=0, column=0)
usuario_entrada = tk.Entry(frame)
usuario_entrada.grid(row=0, column=1)

tk.Label(frame, text="Contraseña:").grid(row=1, column=0)
contraseña_entrada = tk.Entry(frame, show="*")
contraseña_entrada.grid(row=1, column=1)

tk.Button(frame, text="Ingresar", command=bienvenido).grid(row=2, column=0, columnspan=2)

etiqueta_usuario = tk.Label(frame, text="")
etiqueta_usuario.grid(row=3, column=0, columnspan=2)

ventana.mainloop()
