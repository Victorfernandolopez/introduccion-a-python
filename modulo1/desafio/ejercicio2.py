"""
Ejercicio 2
Hacer un programa que determine si una
persona es menor de edad o mayor de edad,
teniendo la edad en una variable.
Probar el código cambiando el valor de la
variable “edad”.
"""

edad=20
if edad >= 18:
    if edad >= 21:
        print("Eres adulto y mayor de 21 años.")
    else:
        print("Eres adulto pero menor de 21 años.")
else:
    print("Eres menor de edad.")