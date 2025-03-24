def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2

def validar_datos():
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Ingrese un número válido.", end=" ")

