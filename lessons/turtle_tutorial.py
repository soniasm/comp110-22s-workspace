"""Turtle Tutorial."""

from turtle import Turtle, colormode, done


leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

colormode(255)

leo.fillcolor(134, 141, 138)


leo.speed(50)
leo.hideturtle()


i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()

bob.penup()
bob.goto(45, 60)

bob.speed(70)
bob.hideturtle()

bob.pencolor(29, 29, 29)


side_length: float = 300
bob.pendown()

while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

i: int = 0
while (i < 20):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.95
    i = i + 1

done()