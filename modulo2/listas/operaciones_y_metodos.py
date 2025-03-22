"""
Las listas tienen métodos incorporados muy útiles:

Método	                    Descripción	                            Ejemplo

len(lista)	                Obtiene el tamaño de la lista	        len(frutas) → 3
lista.append(valor)	        Agrega un elemento al final	            frutas.append("mango")
lista.insert(pos, valor)	Inserta en una posición específica	    frutas.insert(1, "pera")
lista.remove(valor)	        Elimina un valor	                    frutas.remove("banana")
lista.pop(indice)	        Elimina un elemento por índice	        frutas.pop(2)
lista.sort()	            Ordena la lista	                        numeros.sort()
lista.reverse()	            Invierte el orden	                    frutas.reverse()
"""

#Ejemplo de uso de métodos
frutas = ["manzana", "banana", "cereza"]
numeros = [1, 2, 3, 4, 5]

print(len(frutas))  # 3
frutas.append("mango")
print(frutas)  # ['manzana', 'banana', 'cereza', 'mango']
frutas.insert(1, "pera")
print(frutas)  # ['manzana', 'pera', 'banana', 'cereza', 'mango']
frutas.remove("banana")
print(frutas)  # ['manzana', 'pera', 'cereza', 'mango']
frutas.pop(2)
print(frutas)  # ['manzana', 'pera', 'mango']
frutas.sort
print(frutas)  # ['manzana', 'mango', 'pera']
frutas.reverse()
print(frutas)  # ['pera', 'mango', 'manzana']
numeros.sort()
print(numeros)  # [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]
