from random import randint
from turtle import Turtle, Screen, colormode


mbe = Turtle()
mbe.speed(100)
mbe.penup()
mbe.hideturtle()
colormode(255)
mbe.setheading(225)
mbe.forward(300)
mbe.setheading(0)

for _ in range(10):
    for _ in range(10):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        fillcolor = (r, g, b)
        mbe.dot(20, fillcolor)
        mbe.forward(50)
    mbe.left(90)
    mbe.forward(50)
    mbe.left(90)
    mbe.forward(500)
    mbe.setheading(0)


screen = Screen()
screen.exitonclick()
