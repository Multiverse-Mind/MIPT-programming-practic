import turtle


def halfcircle(k):
    n = 50
    for i in range(n // 2):
        turtle.forward(k)
        turtle.right(180 - (((n - 2) * 180) / n))


turtle.shape('turtle')
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)
for i in range(5):
    halfcircle(6)
    halfcircle(1)
halfcircle(6)