"""
.grid() te permite colocar widgets en filas y columnas, como en una tabla
"""
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Usuario:").grid(row=0, column=0)
tk.Entry(ventana).grid(row=0, column=1)

ventana.mainloop()

"""
Reglas de .grid():
Se usa dentro de un mismo contenedor (por ejemplo, una ventana o un frame).

No mezcles .pack() y .grid() en el mismo contenedor.
"""