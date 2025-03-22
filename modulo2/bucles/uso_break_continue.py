#break: termina el bucle
#continue: salta a la siguiente iteracion del bucle
#ejemplo:
for i in range(10):
    if i == 5:
        break
    print(i)
#output:
#0
#1
#2
#3
#4
#cuando i vale 5, el bucle se termina


for i in range(5):
    if i == 2:
        continue
    print(i)

#output:
#0
#1
#cuando i vale 2, se salta a la siguiente iteracion
#3
#4