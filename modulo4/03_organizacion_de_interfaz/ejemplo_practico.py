import tkinter as tk

ventana = tk.Tk()

frame = tk.Frame(ventana)
frame.pack()

tk.Label(frame, text="Nombre:").grid(row=0, column=0)
entrada = tk.Entry(frame)
entrada.grid(row=0, column=1)

tk.Button(frame, text="Enviar").grid(row=1, column=0, columnspan=2)

ventana.mainloop()
