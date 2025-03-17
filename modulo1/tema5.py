# tipos de datos

"""
Mini proyecto 5: Tipos de datos y conversión
Objetivo: Practicar la declaración de variables con diferentes tipos de datos y realizar algunas conversiones de tipos.

Instrucciones:

Crea un programa que pida al usuario su edad (como texto) y la convierta a un número entero.
Luego, imprime la edad multiplicada por 2.
Pide al usuario su nombre y muestra un saludo personalizado.
"""

# Solicitar la edad al usuario como texto
edad = input("Por favor, ingrese su edad: ")

# Convertir la edad a un número entero
edad = int(edad)

# Imprimir la edad multiplicada por 2
print("Su edad multiplicada por 2 es:", edad * 2)

# Solicitar el nombre al usuario
nombre = input("Por favor, ingrese su nombre: ")

# Imprimir un saludo personalizado
print("Hola,", nombre, "¡Bienvenido!")