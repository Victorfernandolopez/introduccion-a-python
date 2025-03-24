#local: solo existe dentro de la función
#global: existe en todo el programa

x = 10  # variable global

def mostrar():
    x = 5  # variable local
    print(x)

mostrar()  # 5
print(x)   # 10
