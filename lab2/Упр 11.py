import turtle


def circle(k):
    n = 50
    for i in range(n):
        turtle.forward(3 + k)
        turtle.left(180 - (((n - 2) * 180) / n))


turtle.shape('turtle')
turtle.left(90)
k = 0
for i in range(10):
    circle(k)
    turtle.left(180)
    circle(k)
    turtle.left(180)
    k += 1