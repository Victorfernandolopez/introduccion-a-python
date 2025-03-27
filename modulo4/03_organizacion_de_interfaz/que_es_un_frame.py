"""
un frame es como una caja contenedora para widgets. sirve para organizar la interfaz en secciones
"""
import tkinter as tk

ventana = tk.Tk()

frame_superior = tk.Frame(ventana)
frame_superior.pack()

ventana.mainloop()