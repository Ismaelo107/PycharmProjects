palabras = ["sol", "luna", "marte", "plutón", "saturno", "dia"]
palabras_mayores = 0

for palabra in range(len(palabras)):

    if len(palabras) > 4:
        palabras_mayores += 1
print(palabras_mayores)
