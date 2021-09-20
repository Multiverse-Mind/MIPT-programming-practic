import turtle


def circle(k):
    n = 50
    for i in range(n):
        turtle.forward(k)
        turtle.left(180 - (((n - 2) * 180) / n))


def halfcircle(k):
    n = 50
    for i in range(n // 2):
        turtle.forward(k)
        turtle.right(180 - (((n - 2) * 180) / n))


turtle.shape('turtle')
turtle.begin_fill()
circle(7)
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(-15, 70)
turtle.pendown()
turtle.begin_fill()
circle(1)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(25, 70)
turtle.pendown()
turtle.begin_fill()
circle(1)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(5, 60)
turtle.right(90)
turtle.pendown()
turtle.width(10)
turtle.forward(15)
turtle.penup()
turtle.goto(30, 35)
turtle.pendown()
turtle.color('red')
halfcircle(3)