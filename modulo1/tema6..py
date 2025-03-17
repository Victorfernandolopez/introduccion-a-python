# operaciones basicas

"""
Mini proyecto 6: Operaciones básicas
Objetivo: Practicar operaciones aritméticas, con cadenas y comparaciones.

Instrucciones:

Crea un programa que haga lo siguiente:
Pida al usuario dos números.
Realice una suma, resta, multiplicación y división de los dos números y muestre los resultados.
Pida al usuario una palabra y repítela tres veces.
Compara si el primer número ingresado es mayor que el segundo e imprime el resultado.
"""

# solicitar dos numeros
num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))

# realizar operaciones aritmeticas
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
multiplicacion = num1 * num2
potencia = num1**num2

print(f"la suma de {num1} + {num2} es: {suma}")
print(f"la resta de {num1} - {num2} es: {resta}")
print(f"la division de {num1} / {num2} es: {division}")
print(f"la division entera de {num1} // {num2} es: {division_entera}")
print(f"El modulo de {num1} % {num2} es: {modulo}")
print(f"la multiplicacion de {num1} * {num2} es: {multiplicacion}")
print(f"la potencia de {num1}**{num2} es: {potencia}")

#triplicar palabra ingresada
palabra = input("ingrese una palabra")
palabra_trplicada = palabra*3
print(palabra_trplicada)

#comparar numeros ingresados
print(f"el numero {num1} es mayor que {num2}? : {num1>num2}")
