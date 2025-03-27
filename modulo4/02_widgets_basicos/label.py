import tkinter as tk
ventana = tk.Tk()

etiqueta = tk.Label(ventana,text="¡hola!")
etiqueta.pack()

ventana.mainloop()

#text: define el texto que se muestra
# .pack(): coloca el widget automaticamente debajo del anterior