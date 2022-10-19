import random

lista = []
aux = 0

for x in range(10):
    lista.append((random.randint(0, 20)))

for x in lista:
    if x > aux:
        aux = x
print(aux)
