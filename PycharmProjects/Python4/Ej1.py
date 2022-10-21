frase = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
spc = 0
for x in range(len(frase)):
    if frase[x] == " ":
        spc += 1
print("Palabras: ", spc + 1)
