import random

lista = []
listaOrd = []

for x in range(10):
    lista.append(random.randint(0, 20))
print(lista)

while (len(lista) > 0):
    aux = 0
    for x in range(len(lista)):
        if lista[x] > aux:
            aux = lista[x]
    lista.remove(aux)
    listaOrd.append(aux)
print(listaOrd)
