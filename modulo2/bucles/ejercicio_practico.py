"""
Ejercicio Práctico
Crea un programa en Python que:

Pida al usuario una cantidad de números a ingresar.
Use un bucle for para cargar esos números en una lista.
Use un bucle while para eliminar todos los números menores a 10.
Muestre la lista resultante.
"""
#funcion para validar que el usuario ingrese un numero
def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

#1. Solicitar al usuario una cantidad de números a ingresar.
print("Ingrese la cantidad de números que desea ingresar:")
cantidad = ingresar_numero()
numeros = []
print(f"ingrese {cantidad} numeros")

#2. Usar un bucle for para cargar los números en una lista.
for i in range(cantidad):
    numero = ingresar_numero()
    numeros.append(numero)

#3. Usar un bucle while para eliminar los números menores a 10.
i = 0
while i < len(numeros):
    if numeros[i] < 10:
        numeros.pop(i)
    else:
        i += 1

#4. Mostrar la lista resultante.
print("\nLista filtrada (mayores o iguales a 10):")
for n in numeros:
    print(f"- {n}")
