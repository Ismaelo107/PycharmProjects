n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))
n3 = int(input("Introduce un número: "))
aux = 0

if n2 > n1:
    aux = n2
else:
    aux = n1

if aux > n3:
    print(f"{aux} es el número más grande")
else:
    print(f"{n3} es el número más grande")
