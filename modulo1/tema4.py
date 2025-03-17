# fundamentos del lenguaje

"""
Mini proyecto 4: Fundamentos básicos
Objetivo: Practicar lo aprendido sobre sintaxis, variables, operadores y funciones.

Instrucciones:

Crea un programa que pida al usuario su nombre y edad.
Almacena esa información en variables.
Usa una función para imprimir un mensaje con su nombre y edad.
Realiza una operación matemática con las variables y muestra el resultado (por ejemplo, suma o resta de edades).
"""

nombre = input("Cual es tu nombre? ")
edad = int(input("Cual es tu edad? "))

def mensaje(nombre, edad):
    print(f"Tu nombre es {nombre} y tienes {edad} años")

mensaje(nombre, edad)

print(f"El doble de tu edad es: {edad + edad}")