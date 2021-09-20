import turtle


n = 100
turtle.shape('turtle')
for i in range(n):
    turtle.forward(10)
    turtle.left(180 - (((n - 2) * 180) / n))  