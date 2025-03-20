"""
1. Tipos de Errores en Python
Los errores en Python pueden clasificarse en tres categorías principales:

1.1. Errores de Sintaxis (SyntaxError)
Ocurren cuando el código no sigue las reglas del lenguaje.

Ejemplo:
"""
print("Hola")  # ❌ Falta el paréntesis de cierre
#Corrección:
print("Hola")  # ✅ Código correcto
"""
1.2. Errores en Tiempo de Ejecución (RuntimeError)
Aparecen cuando el código se ejecuta, pero algo inesperado sucede.

Ejemplo: División por cero (ZeroDivisionError)
"""

num = 10 / 0  # ❌ No se puede dividir entre cero
#Corrección:
num = 10 / 2  # ✅ Corrección: divisor diferente de cero

"""
1.3. Errores Lógicos
El código se ejecuta sin errores, pero los resultados son incorrectos.

Ejemplo:
"""

num1 = 10
num2 = 5
resultado = num1 - num2  # ❌ El usuario quería hacer una suma
print(resultado)  # Devuelve 5, pero debería ser 15
#Corrección:
resultado = num1 + num2  # ✅ Corrección: usar el operador correcto

"""
2. Manejo de Errores con try-except
Podemos prevenir que un programa se detenga usando try-except.

Ejemplo 1: Manejo de ValueError
"""

try:
    edad = int(input("Ingrese su edad: "))
    print(f"Tienes {edad} años.")
except ValueError:
    print("❌ Error: Debes ingresar un número entero.")

#Ejemplo 2: Capturar Múltiples Errores
try:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
except ValueError:
    print("❌ Error: Debes ingresar solo números.")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre 0.")

"""
3. Depuración de Código con IA
Actualmente, existen herramientas que ayudan a detectar y corregir errores automáticamente. Algunas opciones incluyen:

GitHub Copilot (completa código y sugiere correcciones).
ChatGPT (explica errores y sugiere soluciones).
Pylint (analiza código y da recomendaciones de estilo).
debugger de VS Code (permite ejecutar código paso a paso para detectar errores).
Ejemplo de Uso de ChatGPT para Depuración
Si tienes este código con error:

"""

num1 = input("Ingrese un número: ")
num2 = input("Ingrese otro número: ")
print(num1 + num2)  # ❌ Error: concatena cadenas en lugar de sumarlas

"""
Puedes preguntar a ChatGPT:
"Tengo este código en Python, pero en lugar de sumar los números ingresados, los concatena. ¿Cómo lo corrijo?"

Corrección:
"""
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
print(num1 + num2)  # Ahora realiza la suma correctamente

"""
4. Ejercicio Práctico
Escribe un programa en Python que:

Solicite dos números al usuario.
Realice una división entre ellos.
Maneje los siguientes errores:
Entrada de datos incorrecta (ValueError).
División entre cero (ZeroDivisionError).
Muestre el resultado o un mensaje de error adecuado.
"""

# Solicitar al usuario dos números y manejar errores
while True:
    try:
        num1 = float(input("Ingrese el primer número: ").strip())
        break
    except ValueError:
        print("❌ Error: Por favor, ingrese un número válido.")

while True:
    try:
        num2 = float(input("Ingrese el segundo número: ").strip())
        if num2 == 0:
            print("❌ Error: No se puede dividir entre cero. Ingrese otro número.")
            continue  # Pedir de nuevo solo el segundo número
        break
    except ValueError:
        print("❌ Error: Por favor, ingrese un número válido.")

# Realizar la división
resultado = num1 / num2
print(f"✅ El resultado de {num1} / {num2} es: {resultado}")

"""
Revisión de tu Código
Tu código es funcional, robusto y maneja bien los errores. Algunas mejoras posibles:

Uso de strip() en input() para evitar espacios en blanco accidentales.
Explicar mejor el error de ZeroDivisionError cuando ocurre.
Permitir reingresar solo num2 si es 0 en lugar de pedir ambos números de nuevo.
"""
