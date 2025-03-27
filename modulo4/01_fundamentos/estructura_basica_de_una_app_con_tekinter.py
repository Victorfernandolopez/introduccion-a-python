import tkinter as tk

ventana = tk.Tk()             # Crea la ventana principal
ventana.title("Mi App")       # Establece el título de la ventana
ventana.geometry("300x200")   # Establece tamaño: ancho x alto
ventana.mainloop()            # Inicia el "bucle de eventos"

"""
Explicación línea por línea
Línea	                    ¿Qué hace?
import tkinter as tk	    Importa la librería y la nombra tk para usarla más fácil.
tk.Tk()	                    Crea la ventana principal (solo se debe tener una por app).
.title("...")	            Cambia el texto del título de la ventana.
.geometry("300x200")	    Define el tamaño en pixeles: ancho x alto.
.mainloop()	                Inicia el bucle de eventos, que mantiene la ventana abierta y escuchando acciones del usuario.
"""