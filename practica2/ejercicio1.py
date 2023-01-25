print("Ingrese un valor para el lado del cuadrado: ")
lado=int(input())

for i in range(0,lado): #0123
    for j in range(0,lado):
        print("*",end="")
    print()