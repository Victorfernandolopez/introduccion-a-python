#tupla con dias de la semana
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

#diccionario de 3 personas nombre[clave] y edad[valor]
personas = {
    "ana" : 30,
    "juan" : 25,
    "luis" : 35
}

#funcion para validar que el usuario ingrese un numero
def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: ").strip())
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

#menu(agregar,modificar,eliminar,mostrar) para el diccionario de personas
while True:
    print("\nMenú de opciones:")
    print("1. Agregar persona")
    print("2. Modificar edad de persona")
    print("3. Eliminar persona")
    print("4. Mostrar personas")
    print("5. Salir")
    opcion = ingresar_numero()

    if opcion == 1:
        nombre = input("Ingrese el nombre de la persona: ").strip().lower()
        edad = ingresar_numero()
        personas[nombre] = edad
    elif opcion == 2:
        nombre = input("Ingrese el nombre de la persona: ").strip().lower()
        if nombre in personas:
            edad = ingresar_numero()
            personas[nombre] = edad
        else:
            print("La persona no existe.")
    elif opcion == 3:
        nombre = input("Ingrese el nombre de la persona: ").strip().lower()
        if nombre in personas:
            del personas[nombre]
        else:
            print("La persona no existe.")
    elif opcion == 4:
        print("\nPersonas:")
        for nombre, edad in personas.items():
            print(f"{nombre} → {edad}")
    elif opcion == 5:
        break
    else:
        print("Opción inválida.")