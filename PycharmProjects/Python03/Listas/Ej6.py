import random

long = int(input("Introducir lóngitud de lista: "))
lista = []
ini = 0
rep = 0

for x in range(long):
    rand = random.randint(0, 10)
    lista.append(rand)
    ini = lista[0]
    if ini == lista[x]:
        rep += 1
print(lista)
print(rep)
