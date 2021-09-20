import turtle
from math import sin, cos


turtle.shape('turtle')
fi = 0
k = 1
r = 0
dfi = 0.1
while fi <= 100:
    turtle.goto(r * cos(fi), r * sin(fi))
    turtle.left(dfi)
    fi += dfi
    r = k * fi