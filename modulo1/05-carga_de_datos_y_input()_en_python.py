"""
Uso de input()
La función input() permite al usuario ingresar información durante la ejecución del programa. Todo lo que se ingresa por input() es tratado como texto (str), a menos que lo convirtamos a otro tipo.

Ejemplo:
"""
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)

"""
Salida:
Ingrese su nombre: Juan
Hola, Juan

Conversión de Tipos de Datos
Dado que input() siempre devuelve una cadena (str), debemos convertir los datos cuando sea necesario.

Conversión	Función	Ejemplo
A entero (int)	int()	edad = int(input("Ingrese su edad: "))
A decimal (float)	float()	altura = float(input("Ingrese su altura: "))
A cadena (str)	str()	nombre = str(input("Ingrese su nombre: "))
A booleano (bool)	bool()	activo = bool(input("Está activo? (True/False): "))
Ejemplo de Conversión Correcta
"""
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"Tienes {edad} años y mides {altura} metros.")

"""
Errores Comunes y Manejo de Errores
Error al ingresar un tipo incorrecto
Si el usuario ingresa texto en lugar de un número, Python generará un error:

edad = int(input("Ingrese su edad: "))  
# Si el usuario ingresa "veinte", se producirá un error ValueError.
Solución: Usar try-except para manejar errores.

"""
try:
    edad = int(input("Ingrese su edad: "))
    print("Edad ingresada correctamente.")
except ValueError:
    print("Error: Debe ingresar un número entero.")

"""
Manejo de bool() correctamente
Como vimos antes, bool(input()) siempre devuelve True, salvo que la entrada esté vacía.
Solución: Convertir la entrada a minúsculas y compararla con "true".

"""
respuesta = input("¿Está activo? (True/False): ").strip().lower()
activo = respuesta == "true"
print(f"Estado: {activo}")  # True si el usuario ingresó "true"


"""
4. Ejercicio Práctico
Crea un programa en Python que:

Solicite al usuario su nombre, edad, altura y si tiene carnet de conducir (True/False).
Muestre todos los datos ingresados con su tipo de dato.
Maneje errores en la entrada de datos (si el usuario ingresa algo incorrecto, mostrar un mensaje y pedirlo de nuevo).
Ejemplo de salida esperada:

Ingrese su nombre: Ana
Ingrese su edad: 25
Ingrese su altura en metros: 1.65
¿Tienes carnet de conducir? (True/False): true

Nombre: Ana (str)
Edad: 25 (int)
Altura: 1.65 (float)
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

#solicitar altura al usuario y manejar errores
while True:
    try:
        altura = float(input("Ingrese su altura en metros: "))
        break
    except ValueError:
        print("Por favor, ingrese un número decimal.")
        
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
print(f"Altura: {altura} ({type(altura).__name__})")
print(f"Carnet de conducir: {carnet} ({type(carnet).__name__})")