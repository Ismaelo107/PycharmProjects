import random
import turtle
from random import randint

# Preparación de la escena
escena = turtle.Screen()
escena.setup(700, 400)
escena.bgcolor(0.5, 0.5, 0.5)  # RGB

# Preparación del escenario
meta = turtle.Turtle()
meta.hideturtle()
meta.color(0.5, 0.5, 0.5)
meta.penup()
meta.setposition(200, 200)
meta.color(0.1, 0.1, 0.1)
meta.pendown()
meta.right(90)
meta.forward(500)

# Preparación de tortugas
tortugas = []
for x in range(5):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(0.9, 0.1, 0.1)
    tortuga.penup()
    tortuga.speed(5)
    tortuga.speed(random.random()+50)
    tortugas.append(tortuga)

colores = ["red", "blue", "yellow", "orange", "green"]

for x in range(5):
    tortugas[x].hideturtle()
    tortugas[x].setposition(-300, -100 + (30 * x))
    tortugas[x].showturtle()
    tortugas[x].color(colores[x])

# Comienzo del juego
for turno in range(80):
    for x in range (5):
        tortugas[x].forward(randint(5, 10))

        if x==3:
            tortugas[x].forward(5)

# Repetición de la escena
escena.mainloop()
