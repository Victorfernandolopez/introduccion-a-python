"""
Operadores Aritméticos
Estos operadores se utilizan para realizar cálculos matemáticos.

Operador    Descripción	                    Ejemplo	    Resultado
+	        Suma	                        5 + 3	    8
-	        Resta	                        10 - 4	    6
*	        Multiplicación	                2 * 3	    6
/	        División (siempre da float)	    10 / 2	    5.0
- //	    División entera	                10 // 3	    3
%	        Módulo (resto de la división)	10 % 3	    1
**	        Exponente	                    2 ** 3	    8
"""
# Ejemplo de uso de operadores aritméticos
a = 10
b = 3

print("Suma:", a + b)  # 13
print("Resta:", a - b)  # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)  # 3.3333...
print("División entera:", a // b)  # 3
print("Módulo:", a % b)  # 1
print("Exponente:", a ** b)  # 1000

"""
Operadores de Comparación
Comparan dos valores y devuelven True o False.

Operador	Descripción	    Ejemplo	    Resultado
==	        Igualdad	    5 == 5	    True
- !=	    Diferente	    5 != 3	    True
>	        Mayor que	    10 > 3	    True
<	        Menor que	    4 < 7	    True
>=	        Mayor o igual	5 >= 5	    True
<=	        Menor o igual	3 <= 2	    False
"""
# Ejemplo de uso de operadores de comparación
x = 10
y = 5

print(x == y)  # False
print(x > y)   # True
print(x <= y)  # False

"""
Operadores Lógicos
Se usan para combinar expresiones booleanas (True o False).

Operador	Descripción	                                    Ejemplo	        Resultado
and	        Verdadero si ambas condiciones son True	        True and False	False
or	        Verdadero si al menos una condición es True	    True or False	True
not	        Invierte el valor booleano	                    not True	    False
"""

# Ejemplo de uso de operadores lógicos
a = 5
b = 10
c = 15

print(a < b and b < c)  # True (ambas condiciones son ciertas)
print(a > b or b < c)  # True (una condición es cierta)
print(not(a < b))  # False (se invierte el resultado)

"""
Operadores de Asignación
Asignan valores a variables y pueden combinarse con operadores aritméticos.

Operador	Equivalente a	Ejemplo	    Resultado
=	        Asignación	    x = 5	    x es 5
+=	        x = x + 3	    x += 3	    x es 8
-=	        x = x - 2	    x -= 2	    x es 6
*=	        x = x * 4	    x *= 4	    x es 24
/=	        x = x / 2	    x /= 2	    x es 12.0
-//=	    x = x // 3	    x //= 3	    x es 4
%=	        x = x % 3	    x %= 3	    x es 1
**=	        x = x ** 2	    x **= 2	    x es 16
"""

# Ejemplo de uso de operadores de asignación
x = 10
x += 5  # Equivalente a x = x + 5
print(x)  # 15

"""
Ejercicio Práctico 4
Crea un programa en Python que:

Solicite al usuario dos números (num1, num2).
Realice y muestre los resultados de todas las operaciones aritméticas entre ellos (+, -, *, /, //, %, **).
Incluya una comparación num1 > num2 y muestre si es True o False.
Ejemplo de salida esperada:

Ingrese el primer número: 8
Ingrese el segundo número: 3

Suma: 11
Resta: 5
Multiplicación: 24
División: 2.6666...
División entera: 2
Módulo: 2
Exponente: 512
¿El primer número es mayor que el segundo?: True
"""

#solicitar al usuario dos números y manejar errores
while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

#realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
exponente = num1 ** num2

#manejar errores para la división
try:
    division = num1 / num2
except ZeroDivisionError:
    division = "No se puede dividir por cero"

try:
    division_entera = num1 // num2
except ZeroDivisionError:
    division_entera = "No se puede dividir por cero"

try:
    modulo = num1 % num2
except ZeroDivisionError:
    modulo = "No se puede dividir por cero"

#mostrar los resultados
print("\nSuma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Exponente:", exponente)
print(f"¿El primer número es mayor que el segundo?: {num1 > num2}" )