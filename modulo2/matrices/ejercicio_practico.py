"""
Crea un programa en Python que:
Solicite al usuario:
Número de filas.
Número de columnas.
Cree una matriz del tamaño solicitado, solicitando cada valor al usuario.
Muestre la matriz resultante de forma tabulada (una fila por línea).
Permita modificar un valor de la matriz:
El usuario indica fila, columna y nuevo valor.
Muestra la matriz actualizada.
"""
#funcion para validar que el usuario ingrese un numero
def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

#1. Solicitar al usuario el número de filas y columnas.
print("Ingrese el número de filas:")
filas = ingresar_numero()
print("Ingrese el número de columnas:")
columnas = ingresar_numero()

#2. Crear la matriz del tamaño solicitado.
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = ingresar_numero()
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(" ".join(str(x) for x in fila))

# 4. Modificar un valor de la matriz
print("\nModificación de la matriz:")
print("Ingrese la fila a modificar (comienza en 0):")
fila_mod = ingresar_numero()
print("Ingrese la columna a modificar (comienza en 0):")
col_mod = ingresar_numero()

# Verificación de índices
if 0 <= fila_mod < filas and 0 <= col_mod < columnas:
    print("Ingrese el nuevo valor:")
    nuevo_valor = ingresar_numero()
    matriz[fila_mod][col_mod] = nuevo_valor
else:
    print("Posición inválida.")

# 5. Mostrar matriz actualizada
print("\nMatriz actualizada:")
for fila in matriz:
    print(" ".join(str(x) for x in fila))
