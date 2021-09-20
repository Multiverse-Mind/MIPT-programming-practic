import turtle


def circle():
    n = 100
    for i in range(n):
        turtle.forward(3)
        turtle.left(180 - (((n - 2) * 180) / n))


turtle.shape('turtle')
for i in range(6):
    circle()
    turtle.left(60)