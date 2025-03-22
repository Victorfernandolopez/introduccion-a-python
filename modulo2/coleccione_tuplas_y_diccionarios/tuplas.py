"""
Una tupla es una colección ordenada, pero inmutable (no se puede modificar después de su creación). Se define usando paréntesis ().
"""

#creacion de tuplas
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")

#acceso a elementos
print(coordenadas[0])  # 10

#desempaquetado de tuplas
x, y = coordenadas
print(x)  # 10
print(y)  # 20


"""
¿Por qué usar tuplas?
Son más rápidas que las listas.
Útiles para representar datos fijos (coordenadas, fechas, claves constantes).
Se pueden usar como claves en diccionarios (las listas no).
"""