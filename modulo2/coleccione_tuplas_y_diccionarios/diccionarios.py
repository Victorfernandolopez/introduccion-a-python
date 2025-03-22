"""
Un diccionario es una colección no ordenada de pares clave:valor.
Se define con llaves {}.
"""
persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera"
}

# acceso a valores
print(persona["nombre"])  # Ana

#agregar/modificar valores
persona["pais"] = "Argentina"  # nuevo
persona["edad"] = 31  # modificar

#eliminar valores
del persona["profesion"]

#recorrer diccionario
for clave, valor in persona.items():
    print(clave, "→", valor)

"""
Métodos útiles
Método	                                    Descripción
dict.keys()	                                Retorna todas las claves
dict.values()	                            Retorna todos los valores
dict.items()	                            Retorna pares clave:valor
dict.get(clave, valor_predeterminado)	    Acceso seguro
"""