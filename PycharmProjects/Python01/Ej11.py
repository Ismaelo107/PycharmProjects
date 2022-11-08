n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))
dif = 0

if ((n1 > 100) or (n2 > 100)) or ((n1 < 0) or (n2 < 0)):
    print("Error")
else:
    if (n2 > n1):
        print(f"{n2}>{n1}")
        dif = n2 - n1
        print(f"La diferencia es {dif}")
    else:
        print(f"{n2}<{n1}")
        dif = n1 - n2
        print(f"La diferencia es {dif}")

