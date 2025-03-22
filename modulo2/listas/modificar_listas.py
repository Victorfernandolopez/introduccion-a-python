#las listas son mutables, es decir, se pueden modificar

frutas = ["manzana", "banana", "cereza"]
frutas[1] = "naranja"
print(frutas)  # ['manzana', 'naranja', 'cereza']

#tambien podemos agregar y eliminar elementos

#agregar elementos
frutas.append("uva")#agregamos al final
frutas.insert(1, "fresa")#insertamos en la posicion 1
print(frutas) # ['manzana', 'fresa', 'naranja', 'cereza', 'uva']

#eliminar elementos
frutas.remove("fresa")#eliminamos la fresa
frutas.pop(1)#eliminamos el elemento en la posicion 1
print(frutas) # ['manzana', 'naranja', 'cereza', 'uva']
