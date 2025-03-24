"""
Ejercicio práctico: Proyecto Modular
Crear un proyecto con 2 archivos:
1. calculadora.py
Contiene las funciones: sumar, restar, multiplicar, dividir.

2. main.py
Importa calculadora y permite:

Pedir dos números.

Mostrar menú.

Ejecutar la operación elegida usando el módulo.
"""

import calculadora as cal

print("ingrese el primer numero", end=" ")
numero1 = cal.validar_datos()
print("ingrese el segundo numero", end=" ")
numero2 = cal.validar_datos()

while True:
    print("\nMenú de operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("Seleccione una opción:", end=" ")
    
    opcion = cal.validar_datos()

    if opcion == 1:
        print(f"Resultado: {cal.sumar(numero1, numero2)}")
    elif opcion == 2:
        print(f"Resultado: {cal.restar(numero1, numero2)}")
    elif opcion == 3:
        print(f"Resultado: {cal.multiplicar(numero1, numero2)}")
    elif opcion == 4:
        print(f"Resultado: {cal.dividir(numero1, numero2)}")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")