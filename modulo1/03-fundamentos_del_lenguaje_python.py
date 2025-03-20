"""
Ejercicio Práctico 3
Escribe un programa en Python que:

Pida al usuario su nombre, edad y si tiene carnet de conducir (True/False).
Muestre los valores ingresados y su tipo de dato usando type().
Formatee la salida con f-strings.
Ejemplo de salida esperada:

Ingrese su nombre: Ana
Ingrese su edad: 25
¿Tienes carnet de conducir? (True/False): True

Nombre: Ana (str)
Edad: 25 (int)
Carnet de conducir: True (bool)
"""
#solicitar nombre al usuario
nombre = input("Ingrese su nombre: ")
#solicitar edad al usuario y manejar errores
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero.")
#solicitar si tiene carnet de conducir al usuario y manejar errores
while True:
    try:
        carnet = input("¿Tiene carnet de conducir? (True/False): ")
        if carnet.lower() == "true":
            carnet = True
            break
        elif carnet.lower() == "false":
            carnet = False
            break
        else:
            raise ValueError
    except ValueError:
        print("Por favor, ingrese True o False.")

#mostrar los valores ingresados y su tipo de dato
print(f"\nNombre: {nombre} ({type(nombre).__name__})")
print(f"Edad: {edad} ({type(edad).__name__})")
print(f"Carnet de conducir: {carnet} ({type(carnet).__name__})")

"""
La función type() devuelve el tipo de dato como un objeto de tipo type, mientras que el atributo __name__ extrae el nombre del tipo como una cadena (str). Esto es útil si deseas mostrar el tipo de dato en un formato legible para los usuarios.

Por ejemplo:

nombre = "Ana"
print(type(nombre))  # <class 'str'>
print(type(nombre).__name__)  # str
"""