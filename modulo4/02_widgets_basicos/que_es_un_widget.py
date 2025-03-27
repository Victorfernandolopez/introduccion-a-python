"""
Un widget es un elemento visual de la interfaz. Puede ser un botón, una etiqueta de texto, un campo para escribir, etc.
Todos los widgets se crean con la misma estructura:

nombre_widget = tk.WidgetClase(ventana, opciones)
nombre_widget.metodo_para_colocar()
"""

#ejemplo

#label:
import tkinter as tk
ventana = tk.Tk()

etiqueta = tk.Label(ventana,text="¡hola!")
etiqueta.pack()

ventana.mainloop()

#text: define el texto que se muestra
# .pack(): coloca el widget automaticamente debajo del anterior