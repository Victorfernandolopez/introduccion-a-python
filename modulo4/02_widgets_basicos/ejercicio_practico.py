"""
Ejercicio práctico: formulario_basico.py
Crea una ventana que:

Tenga una etiqueta: "Ingrese su nombre:"

Tenga un campo de entrada.

Tenga un botón que diga "Saludar".

Al presionar el botón, aparezca otra etiqueta con el mensaje:
"Hola, [nombre ingresado]".
"""

import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"hola, {nombre}")
    #.config() es un método que permite cambiar el texto de una etiqueta en tiempo de ejecución


ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="ingrese su nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()