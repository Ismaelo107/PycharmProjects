import random

vocales = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "m", "n", "p", "s", "t", "v"]
palabras = []


def guardar_lista(lista):
    fichero = open("palabras.txt", "a")
    fichero.write(str(lista))


def generar_palabra(caracter_palabra):
    palabra = ""

    for x in range(caracter_palabra // 2):
        palabra = palabra + consonantes[random.randint(0, len(consonantes) - 1)]
        palabra = palabra + vocales[random.randint(0, len(vocales) - 1)]

    return palabra


def generar_lista_palabras(num_palabras, num_letras):
    lista_palabras = []
    for x in range(num_palabras):
        mi_palabra = generar_palabra(num_letras)
        lista_palabras.append(mi_palabra)
    return lista_palabras


mi_nueva_lista_de_palabras = generar_lista_palabras(14, 80)
print(mi_nueva_lista_de_palabras)
