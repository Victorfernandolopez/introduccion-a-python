"""
Ejercicio Práctico
Escribe un programa en Python que:

Cree una lista con 5 nombres ingresados por el usuario.
Permita al usuario:
Agregar un nuevo nombre.
Eliminar un nombre existente.
Ordenar la lista alfabéticamente.
Muestre la lista final.
"""

#1. Crear una lista vacía para almacenar los nombres.
nombres = []

#2. Solicitar al usuario que ingrese 5 nombres y agregarlos a la lista.
for i in range(5):
    nombres.append(input("ingrese un nombre: "))

#3. Mostrar un menú con las siguientes opciones:
#    1. Agregar un nuevo nombre a la lista.
#    2. Eliminar un nombre existente de la lista.
#    3. Ordenar la lista alfabéticamente.
#    4. Mostrar la lista actual.
#    5. Salir del programa.
opcion = 0

while opcion != 5:
    try:
        print("Menú:")
        print("1. Agregar un nuevo nombre a la lista.")
        print("2. Eliminar un nombre existente de la lista.")
        print("3. Ordenar la lista alfabéticamente.")
        print("4. Mostrar la lista actual.")
        print("5. Salir del programa.")
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    if opcion == 1:
        nombre = input("Ingrese el nombre que desea agregar: ")
        nombres.append(nombre)
    elif opcion == 2:
        nombre = input("Ingrese el nombre que desea eliminar: ")
        if nombre in nombres:#si el nombre esta en la lista lo eliminamos
            nombres.remove(nombre)
        else:
            print("El nombre no está en la lista.")
    elif opcion == 3:
        nombres.sort()
    elif opcion == 4:
        print(nombres)
    elif opcion == 5:
        print("Saliendo del programa...")
