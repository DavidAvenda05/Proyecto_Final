import turtle
import random
import time
import tkinter

vidas=3
puntuacion=0

ventana=turtle.Screen()
ventana.tracer(0)
ventana.title("PACMAN")
ventana.bgcolor("black")
ventana.setup(650,650)

pacman=turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color("yellow")
pacman.shape("circle")
pacman.direction = "stop"

enemigos = []
for x in range (10):
    fantasmas = turtle.Turtle()
    fantasmas.penup()
    fantasmas.color("purple")
    fantasmas.shape("turtle")
    fantasmas.speed = 0.5
    x = random.randint(-280,280)
    y = random.randint (-280,280)
    fantasmas.setposition(x,y)
    enemigos.append(fantasmas)

p = turtle.Turtle()
p.speed(0)
p.penup()
p.color("green")
p.goto(0, 245)
p.pendown()
p.write("Puntuación: {} Vidas: {}".format(puntuacion, vidas), align="center", font=("Times", 36 ))
p.hideturtle() 


alimento = []
for _ in range (40):
    comida = turtle.Turtle()
    comida.speed(0)
    comida.penup()
    comida.color("white")
    comida.shape("circle")
    comida.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    comida.setposition(x,y)
    alimento.append(comida)

def movimiento():
    if pacman.direction == "up":
        y=pacman.ycor()
        y+= 1
        pacman.sety(y)

    if pacman.direction == "down":
        y=pacman.ycor()
        y-= 1
        pacman.sety(y)

    if pacman.direction == "left":
        x=pacman.xcor()
        x-= 1
        pacman.setx(x)

    if pacman.direction == "right":
        x=pacman.xcor()
        x+= 1
        pacman.setx(x)

def fantasmaMovimiento():
    for fantasmas in enemigos:
        x = fantasmas.ycor()
        y = fantasmas.xcor()
        x += fantasmas.speed
        y += fantasmas.speed
        fantasmas.sety(y)
        fantasmas.setx(x)

def moveUp():
    pacman.direction = "up"

def moveDown():
    pacman.direction = "down"

def moveLeft():
    pacman.direction = "left"

def MoveRight():
    pacman.direction = "right"


ventana.listen()
ventana.onkeypress(moveUp, "Up")
ventana.onkeypress(moveDown, "Down")
ventana.onkeypress(moveLeft, "Left")
ventana.onkeypress(MoveRight, "Right")

while True:
    ventana.update()

    if pacman.xcor()>300 or pacman.xcor()<-300 or pacman.ycor()>300 or pacman.ycor()<-300:
        vidas-= 1
        p.clear()
        p.write("Puntuación: {} Vidas: {}".format(puntuacion, vidas), align="center", font=("Times", 36 ))
        time.sleep(1)
        pacman.goto(0, 0)

    if vidas == 0:
        puntuacion=0
        vidas=3
        p.clear()
        p.write("Puntuación: {} Vidas: {}".format(puntuacion, vidas), align="center", font=("Times", 36 ))
        time.sleep(1)
        pacman.goto(0,0)


    for comida in alimento:
        if pacman.distance(comida) < 10:
            puntuacion+=2
            p.clear()
            p.write("Puntuación: {} Vidas: {}".format(puntuacion, vidas), align="center", font=("Times", 36 ))
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            comida.goto(x,y)

    for fantasmas in enemigos:
        if fantasmas.xcor()>300 or fantasmas.xcor()<-300 or fantasmas.ycor()>300 or fantasmas.ycor()<-300:
            x = random.randint(-360, 360)
            y = random.randint(-360, 360)
            fantasmas.goto(x,y)
            fantasmaMovimiento()

    for fantasmas in enemigos:
        if pacman.distance(fantasmas) < 10:
            vidas -= 1
            p.clear()
            p.write("Puntuación: {} Vidas: {}".format(puntuacion, vidas), align="center", font=("Times", 36 ))
            time.sleep(1)
            pacman.goto(0, 0)


    movimiento()
    fantasmaMovimiento()