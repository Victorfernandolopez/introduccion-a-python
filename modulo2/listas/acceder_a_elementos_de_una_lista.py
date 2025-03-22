"""
Podemos acceder a los elementos de una lista usando índices.

Índice	    Elemento	        Índice Negativo
0	        "manzana"       	-3
1	        "banana"	        -2
2	        "cereza"	        -1
"""
frutas = ["manzana", "banana", "cereza"]

print(frutas[0])  # manzana
print(frutas[-1]) # cereza
#Si intentamos acceder a un índice fuera del rango, obtenemos un error:


#print(frutas[5])  #  IndexError