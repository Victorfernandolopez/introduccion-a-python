"""
1. Cuándo usar cada colección
Colección	            ¿Cuándo usarla?
list	                Cuando necesitás almacenar varios elementos mutables y ordenados.
tuple	                Cuando necesitás una colección fija e inmutable. Ideal para coordenadas, colores, fechas, etc.
dict	                Cuando necesitás asociar una clave a un valor. Ideal para representar datos tipo ficha, objetos o registros.
set	                    Cuando necesitás almacenar valores únicos, sin importar el orden.
"""

"""
Comparación entre colecciones
Propiedad	    list	    tuple	       dict	                                        set
Ordenada	    ✅	        ✅	        ❌(desde Python 3.7 mantiene orden)	        ❌
Indexada	    ✅	        ✅	        ❌(por clave)	                            ❌
Mutable	        ✅	        ❌	        ✅	                                        ✅
Duplicados	    ✅	        ✅	        ❌(una sola clave)	                        ❌
Acceso rápido   Por índice	Por índice	   Por clave	                                Por valor
Sintaxis	    []	          ()	       {clave: valor}	                            {valor}
"""

"""
3. Optimización de uso según el caso
¿Solo vas a leer valores fijos? → Tupla.
¿Necesitás buscar por claves? → Diccionario.
¿Querés evitar valores duplicados? → Conjunto (set).
¿Requiere orden y modificación? → Lista.
"""
