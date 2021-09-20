import turtle


turtle.shape('turtle')
n = int(input())
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(360 / n)