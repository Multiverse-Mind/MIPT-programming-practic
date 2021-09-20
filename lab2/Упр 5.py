import turtle


turtle.shape('turtle')
for i in range(10):
    turtle.forward(20 + i * 20)
    turtle.left(90)
    turtle.forward(20 + i * 20)
    turtle.left(90)
    turtle.forward(20 + i * 20)
    turtle.left(90)
    turtle.forward(20 + i * 20)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()