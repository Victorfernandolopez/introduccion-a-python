"""
Ejercicio práctico comparativo
Crea un programa que:

Use una lista para registrar una lista de materias.
Convierta esa lista en una tupla para proteger los datos.
Use un diccionario para asignar una nota a cada materia.
Use un conjunto (set) para mostrar todas las notas únicas.
El programa debe:

Mostrar cada estructura con sus valores.
Explicar qué tipo de colección es y por qué se usó.
"""

# 1. Crear una lista de materias.
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# 2. Convertir la lista en una tupla.
materias_tupla = tuple(materias)

# 3. Crear un diccionario con las notas de cada materia.
notas = {
    "Matemáticas": 7,
    "Física": 8,
    "Química": 9,
    "Historia": 6,
    "Lengua": 8
}

# 4. Crear un conjunto con las notas únicas.
notas_unicas = set(notas.values())# notas.values() retorna una lista con los valores del diccionario, y set() convierte esa lista en un conjunto.

# Mostrar cada estructura con sus valores.
print("Lista de materias:")
print(materias)
print(f"Tipo de colección: Lista")
print("Razón de uso: Se usó una lista para almacenar las materias porque se necesita un orden específico y se pueden modificar los elementos.")

print("\nTupla de materias:")
print(materias_tupla)
print(f"Tipo de colección: Tupla")
print("Razón de uso: Se usó una tupla para proteger los datos de las materias, ya que no deben ser modificados.")

print("\nDiccionario de notas:")
print(notas)
print(f"Tipo de colección: Diccionario")
print("Razón de uso: Se usó un diccionario para asociar una nota a cada materia, permitiendo una búsqueda rápida por clave.")

print("\nConjunto de notas únicas:")
print(notas_unicas)
print(f"Tipo de colección: Conjunto")
print("Razón de uso: Se usó un conjunto para almacenar las notas únicas, evitando duplicados y permitiendo una rápida verificación de valores únicos.")

