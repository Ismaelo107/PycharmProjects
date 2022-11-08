frase = "Hola buenas que tal como"

numPal = len(frase.split())

print("Palabras :", numPal)

palabra = frase.split()

print(palabra)

longPalabra =0

for x in range(len(frase)):
    if len(palabra[x]) > longPalabra:
        longPalabra=len(palabra[x])
print(longPalabra)