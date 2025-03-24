"""
Ejercicio práctico: calculadora_funciones.py
Crea un programa que:

Defina 4 funciones: sumar(), restar(), multiplicar(), dividir().

Cada función debe tomar dos parámetros.

En el programa principal:

Pedí dos números al usuario.

Mostrá un menú para elegir la operación.

Llamá a la función correspondiente.

Mostrá el resultado.


"""

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2

def validar_datos():
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Ingrese un número válido.", end=" ")

# MAIN
print("Ingrese el primer número:", end=" ")
numero1 = validar_datos()
print("Ingrese el segundo número:", end=" ")
numero2 = validar_datos()

while True:
    print("\nMenú de operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("Seleccione una opción:", end=" ")
    
    opcion = validar_datos()

    if opcion == 1:
        print(f"Resultado: {sumar(numero1, numero2)}")
    elif opcion == 2:
        print(f"Resultado: {restar(numero1, numero2)}")
    elif opcion == 3:
        print(f"Resultado: {multiplicar(numero1, numero2)}")
    elif opcion == 4:
        print(f"Resultado: {dividir(numero1, numero2)}")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")

