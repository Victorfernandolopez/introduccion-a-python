# condicionales

"""
sintaxix basica:

if condición:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa


condicionales multiples:
if condición1:
    # Código si la condición1 es verdadera
elif condición2:
    # Código si la condición2 es verdadera
else:
    # Código si ninguna de las condiciones anteriores es verdadera


condicionales anidadas:
edad=20
if edad >= 18:
    if edad >= 21:
        print("Eres adulto y mayor de 21 años.")
    else:
        print("Eres adulto pero menor de 21 años.")
else:
    print("Eres menor de edad.")

"""

"""
Mini proyecto 7: Condicionales
Objetivo: Practicar el uso de condicionales para tomar decisiones basadas en la entrada del usuario.

Instrucciones:

Crea un programa que pida al usuario su edad.
Si tiene 18 años o más, el programa debe imprimir "Puedes votar".
Si tiene menos de 18 años, debe imprimir "No puedes votar".
Luego, pregunta al usuario si tiene una identificación oficial. Si la respuesta es "sí", imprime "Puedes votar con tu identificación". Si la respuesta es "no", imprime "No puedes votar sin identificación".
"""

#pedir edad
edad = int(input("ingrese su edad"))
if edad >= 18:
    print("puedes votar")
else:
    print("no puedes votar")

respuesta = input("tiene identificacion oficial")
if respuesta == "si":
    print("puedes votar con identificacion")
else:
    print("no puedes votar sin identificacion")




