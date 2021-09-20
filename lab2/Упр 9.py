import turtle
from math import sin, pi


def polygon(n, r):
    for i in range(n):
        turtle.forward(2 * r * sin(2 * pi / (2 * n)))
        turtle.left(180 - (((n - 2) * 180) / n))


turtle.shape('turtle')
turtle.penup()
r = 20
turtle.forward(r)
turtle.pendown()
for n in range(3, 13):
    turtle.left(180 - (((n - 2) * 180) / (n * 2)))
    polygon(n, r)
    turtle.right(180 - (((n - 2) * 180) / (n * 2)))
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()    
    r += 10