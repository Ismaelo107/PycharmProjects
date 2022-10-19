import random
from os import remove

lista = []
listaOrd = []

for x in range(10):
    lista.append((random.randint(0, 20)))
print(lista)

for x in lista:
    aux = 0
    if x > aux:
        aux = x
        del lista[aux]
        listaOrd.append(aux)
print(listaOrd)
