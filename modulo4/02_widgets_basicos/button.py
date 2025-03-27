import tkinter as tk

def saludar():
    print("¡hola!")


ventana = tk.Tk()

boton =  tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()

#text: texto que aparece en el boton
#command: funcion que se ejecuta al hacer click
#¡no se ponen parentesis en command=saludar!