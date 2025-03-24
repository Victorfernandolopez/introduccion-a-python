"""
Un módulo es cualquier archivo .py que contiene funciones, clases o variables que pueden importarse y usarse desde otros archivos.
"""

# ejemplo:
# suponiendo que en el archivo operaciones.py tenemos funciones de operaciones matematicas (suma,resta,multiplicacion, division etc...)
"""
def sumar(a, b):
    return a + b
""" 

# ahora en nuestro archivo actual  que se llama main.py queremos usar una de las funciones que tenemos en el archivo operaciones.py, lo aremos de la siguiente forma

"""
import operaciones

resultado = operaciones.sumar(5, 3)
print(resultado)  # 8
"""