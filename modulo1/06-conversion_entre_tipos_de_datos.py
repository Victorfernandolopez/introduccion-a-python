"""
1. Conversión Implícita (Automática)
Python realiza conversiones de tipos de datos de forma automática cuando no hay pérdida de información.

Ejemplo: Conversión int → float
"""

entero = 5
decimal = entero + 2.5  # Python convierte 5 a 5.0 automáticamente
print(decimal)  # 7.5
print(type(decimal))  # <class 'float'>

"""
Regla general: Python convierte automáticamente tipos más pequeños a tipos más grandes (int → float → complex).

Conversión automática en expresiones booleanas
"""

print(True + 5)  # 6 (True se convierte a 1)
print(False + 3)  # 3 (False se convierte a 0)

"""
2. Conversión Explícita (Casting)
Cuando Python no puede hacer una conversión automática, debemos forzarla mediante int(), float(), str(), bool(), etc.

Conversión	Función	Ejemplo
A entero	int()	int("10") → 10
A decimal	float()	float("3.14") → 3.14
A cadena	str()	str(25) → "25"
A booleano	bool()	bool(0) → False, bool(1) → True
Ejemplo: Convertir str a int
"""

num_texto = "20"
num = int(num_texto)  # Convierte "20" en 20
print(num + 5)  # 25


#Ejemplo: Convertir float a int
decimal = 3.99
entero = int(decimal)  # Se trunca a 3 (no redondea)
print(entero)

"""
3. Errores Comunes en la Conversión
3.1. Error al convertir texto a número
"""

print(int("hola"))  # ❌ ValueError: invalid literal for int()
#Solución: Validar antes de convertir.


#3.2. Convertir float a int sin redondeo
print(int(5.9))  # 5 (No redondea, solo trunca)

#Solución:
import math
print(math.ceil(5.9))  # 6 (Redondea hacia arriba)
print(math.floor(5.9))  # 5 (Redondea hacia abajo)

#3.3. Convertir str a bool
print(bool("False"))  # True (porque la cadena no está vacía)

#Solución:
respuesta = input("Ingrese True o False: ").strip().lower()
booleano = respuesta == "true"  # Compara directamente con "true"
print(booleano)

"""
4. Ejercicio Práctico
Escribe un programa en Python que:

Solicite al usuario:
Un número entero
Un número decimal
Un valor booleano (True/False)
Convierta los valores ingresados al tipo de dato correspondiente.
Muestre los valores originales y convertidos con su tipo de dato.
Ejemplo de salida esperada

Ingrese un número entero: 15
Ingrese un número decimal: 3.5
Ingrese un valor booleano (True/False): true

Número entero: 15 (int)
Número decimal: 3.5 (float)
Valor booleano: True (bool) booleano: True (bool)

"""

#solicitar número entero al usuario
while True:
    try:
        num_entero = int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero.")

#solicitar número decimal al usuario
while True:
    try:
        num_decimal = float(input("Ingrese un número decimal: "))
        break
    except ValueError:
        print("Por favor, ingrese un número decimal.")

# Solicitar valor booleano al usuario con validación
while True:
    valor = input("Ingrese un valor booleano (True/False): ").strip().lower()
    if valor in ["true", "false"]:
        booleano = valor == "true"
        break
    print("Error: Debe ingresar 'True' o 'False'.")

# Mostrar los valores originales y convertidos con su tipo de dato
print("\n Datos ingresados:")
print(f"Número entero: {num_entero} ({type(num_entero).__name__})")
print(f"Número decimal: {num_decimal} ({type(num_decimal).__name__})")
print(f"Valor ingresado: {valor} ({type(valor).__name__})")
print(f"Valor booleano convertido: {booleano} ({type(booleano).__name__})")
