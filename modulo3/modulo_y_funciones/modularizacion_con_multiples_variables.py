#organizar el codigo en bloques de funciones permite
# separar la logicas de los programas
# reutilizar codigo
# facilitar el mantenimiento

def pedir_datos():
    nombre = input("Ingrese su nombre: ")
    return nombre

def saludar(nombre):
    print(f"¡Hola, {nombre}!")

nombre = pedir_datos()
saludar(nombre)
