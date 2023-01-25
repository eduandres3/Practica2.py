Lista_nombres = ["rosa", "percy", "angie", "abigail", "esther"]
lista=[]
for x in range(5):
    valor=int(input("Ingrese el valor de su edad: "))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista de Nombres respectivamente: ")
print(Lista_nombres)
print("Lista de edades: ")
print(lista)

print("La mayor edad de lista es: ")
print(mayor)

nombre = input("Dígame su nombre en minuscula: ")
if nombre in Lista_nombres:
  print("Su nombre si fugura en la lista")
else:
  print("No figura en la lista")
