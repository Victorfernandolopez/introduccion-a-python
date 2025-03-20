"""
Ejercicio Práctico 1
Escribe un programa en Python que solicite al usuario dos números y muestre su multiplicación.

Una vez que lo hayas intentado, dime si necesitas ayuda o si quieres validarlo conmigo.
"""

# Solicitar datos al usuario con manejo de errores
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")
        num1 = int(num1)
        num2 = int(num2)
        break
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
print("El resultado de la multiplicación es:", num1 * num2)