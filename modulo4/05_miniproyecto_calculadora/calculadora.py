"""
Mini Proyecto 1: Calculadora visual
Requisitos funcionales:
La app debe mostrar dos campos para ingresar números.
Debe tener 4 botones: Sumar, Restar, Multiplicar, Dividir.
Al presionar uno, debe mostrar el resultado debajo.
Los campos deben limpiarse automáticamente luego de la operación.

Estructura recomendada:
Usar StringVar para los dos campos de entrada.
Usar Label para mostrar el resultado.
Usar Frame para contener la interfaz ordenadamente.
Validar que los campos no estén vacíos y sean numéricos.

💡 Tip extra:
Usá .try-except para evitar errores al convertir los valores, especialmente para controlar división por cero.

Implementá lo siguiente:

[ Número 1: ______ ]     (Entrada 1)
[ Número 2: ______ ]     (Entrada 2)

[ Sumar ] [ Restar ] [ Multiplicar ] [ Dividir ]

Resultado: [Aquí va el resultado]
"""

import tkinter as tk

#funcion suma
def sumar():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        resultado.config(text=f"Resultado: {n1 + n2}")
        borrar_campos()
    except ValueError:
        resultado.config(text="Error: Ingrese números válidos.")

#funcion resta
def restar():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        resultado.config(text=f"Resultado: {n1 - n2}")
        borrar_campos()
    except ValueError:
        resultado.config(text="Error: Ingrese números válidos.")

#funcion multiplicar
def multiplicar():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        resultado.config(text=f"Resultado: {n1 * n2}")
        borrar_campos()
    except ValueError:
        resultado.config(text="Error: Ingrese números válidos.")

#funcion dividir
def dividir():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        resultado.config(text=f"Resultado: {n1 / n2}")
        borrar_campos()
    except ValueError:
        resultado.config(text="Error: Ingrese números válidos.")
    except ZeroDivisionError:
        resultado.config(text="Error: No se puede dividir por cero.")

#funcion borrar campos
def borrar_campos():
    numero1.set("")
    numero2.set("")


ventana = tk.Tk()
ventana.title("Calculadora visual")

tk.Frame(ventana).grid(row=0, column=0)
numero1 = tk.StringVar()
numero2 = tk.StringVar()

tk.Label(ventana, text="Número 1:").grid(row=1, column=0)
tk.Entry(ventana, textvariable=numero1).grid(row=1, column=1)

tk.Label(ventana, text="Número 2:").grid(row=1, column=2)
tk.Entry(ventana, textvariable=numero2).grid(row=1, column=3)

tk.Button(ventana, text="Sumar", command=sumar).grid(row=2, column=0, columnspan=4)
tk.Button(ventana, text="Restar", command=restar).grid(row=3, column=0, columnspan=4)
tk.Button(ventana, text="Multiplicar", command=multiplicar).grid(row=4, column=0, columnspan=4)
tk.Button(ventana, text="Dividir", command=dividir).grid(row=5, column=0, columnspan=4)

resultado = tk.Label(ventana, text="Resultado:")
resultado.grid(row=6, column=0, columnspan=4)

ventana.mainloop()