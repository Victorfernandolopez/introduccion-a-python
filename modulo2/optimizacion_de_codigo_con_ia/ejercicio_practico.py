"""
Ejercicio Práctico
Tienes el siguiente código repetitivo. Optimízalo usando una comprensión de listas:

pares = []
for i in range(1, 21):
    if i % 2 == 0:
        pares.append(i)

Luego, crea una función numeros_pares(n) que devuelva una lista de los pares hasta n, inclusive.
"""

#comprension de listas
pares = [i for i in range(1, 21) if i % 2 == 0]
print(pares)