import tkinter as tk

def mostrar_valores():
    print(f"Nombre: {nombre_var.get()}")
    print(f"Edad: {edad_var.get()}")
    print(f"Precio: {precio_var.get()}")
    print(f"Activo: {activo_var.get()}")

ventana = tk.Tk()
ventana.title("Variables de Control")

# Crear variables de control
nombre_var = tk.StringVar()
edad_var = tk.IntVar()
precio_var = tk.DoubleVar()
activo_var = tk.BooleanVar()

# Enlazar variables a widgets
tk.Label(ventana, text="Nombre:").pack()
tk.Entry(ventana, textvariable=nombre_var).pack()

tk.Label(ventana, text="Edad:").pack()
tk.Entry(ventana, textvariable=edad_var).pack()

tk.Label(ventana, text="Precio:").pack()
tk.Entry(ventana, textvariable=precio_var).pack()

tk.Label(ventana, text="Activo:").pack()
tk.Checkbutton(ventana, text="¿Activo?", variable=activo_var).pack()

# Botón para mostrar valores
tk.Button(ventana, text="Mostrar valores", command=mostrar_valores).pack()

ventana.mainloop()