import turtle


def star(n):
    for i in range(n):
        turtle.forward(150)
        turtle.right(180 - 180 / n)


turtle.shape('turtle')
star(5)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
star(11)