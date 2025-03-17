"""
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares.
"""

#de enero a julio (7 meses)
suma1 = 300 * 7
#de julio a octubre (3)
suma2 = 500 * 3
#de noviembre a diciembre (2 meses)
suma3 = 700 * 2

total = suma1 + suma2 + suma3

promedio_sueldo = total / 12

if promedio_sueldo >= 900:
    print("su sueldo es mejor de lo normal")
elif promedio_sueldo <900 and promedio_sueldo >=300:
    print("su sueldo es normal")
else:
    print("su sueldo es bajo")

