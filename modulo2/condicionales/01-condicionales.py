"""
1. Uso de if, elif y else
La estructura condicional en Python se basa en if, elif y else.

if condición:
    # Bloque de código si la condición es True
elif otra_condición:
    # Bloque de código si la primera condición es False y esta es True
else:
    # Bloque de código si ninguna condición anterior se cumple
Ejemplo Básico
"""

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")

"""
Salida esperada:

Ingrese su edad: 20
Eres mayor de edad.
"""

"""
2. Expresiones Condicionales (and, or, not)
Podemos combinar condiciones usando and, or y not.

Operador	Descripción	                                        Ejemplo
and	        Devuelve True si ambas condiciones son True	        edad >= 18 and tiene_licencia
or	        Devuelve True si al menos una condición es True	    edad >= 18 or tiene_permiso
not	        Invierte el valor de la condición	                not es_menor
Ejemplo
"""

edad = int(input("Ingrese su edad: "))
tiene_licencia = input("¿Tienes licencia de conducir? (si/no): ").strip().lower() == "si"

if edad >= 18 and tiene_licencia:
    print("Puedes conducir.")
elif edad >= 18 and not tiene_licencia:
    print("Necesitas una licencia para conducir.")
else:
    print("No puedes conducir.")

"""
3. Condicionales Anidados
Podemos usar if dentro de otro if para verificar múltiples condiciones.
Ejemplo
"""
nota = float(input("Ingrese su nota: "))

if nota >= 60:
    print("Aprobaste.")
    if nota >= 90:
        print("¡Felicidades! Tienes una calificación excelente.")
else:
    print("Reprobaste. Debes mejorar.")

"""
4. Expresión Condicional en una Línea (Operador Ternario)
Podemos escribir un if-else en una sola línea.
"""
edad = int(input("Ingrese su edad: "))
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

"""
Esta línea utiliza un operador ternario, una forma compacta de escribir una estructura condicional. Evalúa si la variable edad es mayor o igual a 18. Si la condición es verdadera, asigna la cadena "Mayor de edad" a la variable mensaje; de lo contrario, asigna "Menor de edad". Este enfoque es más conciso que usar una estructura if-else tradicional.
"""


"""
5. Ejercicio Práctico
Escribe un programa que:

Solicite edad y si tiene licencia de conducir (si/no).
Evalúe las siguientes condiciones:
Si la edad es menor de 16, imprimir "No puedes conducir."
Si la edad está entre 16 y 18, imprimir "Puedes conducir con permiso de tus padres."
Si la edad es 18 o más y tiene licencia, imprimir "Puedes conducir."
Si la edad es 18 o más pero no tiene licencia, imprimir "Necesitas una licencia para conducir."
Usa operadores and, or y not en el código.
"""

# Solicitar edad al usuario y manejar errores
while True:
    try:
        edad = int(input("Ingrese su edad: ").strip())  # Limpia espacios
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Solicitar si tiene licencia de conducir al usuario
while True:
    licencia = input("¿Tienes licencia de conducir? (si/no): ").strip().lower()
    if licencia in ["si", "no"]:
        licencia = licencia == "si"  # Convierte a booleano
        break
    print("Error: Debe responder 'si' o 'no'.")

# Evaluar edad y licencia
if edad < 16:
    print("No puedes conducir.")
elif 16 <= edad < 18:
    print("Puedes conducir con permiso de tus padres.")
elif edad >= 18 and licencia:
    print("Puedes conducir.")
else:
    print("Necesitas una licencia para conducir.")

