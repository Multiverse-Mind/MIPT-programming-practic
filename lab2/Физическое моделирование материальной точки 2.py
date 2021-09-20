from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 1000
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
coords = []
speeds = []
for unit in pool:
    unit.penup()
    unit.speed(200)
    x, y = randint(-200, 200), randint(-200, 200)
    coords.append([x, y])
    unit.goto(x, y)
    speeds.append([randint(-10, 10), randint(-10, 10)])
for i in range(steps_of_time_number):
    for j in range(len(pool)):
        unit = pool[j]
        x1, y1 = coords[j][0], coords[j][1]
        vx, vy = speeds[j][0], speeds[j][1]
        x2, y2 = x1 + vx, y1 + vy
        coords[j][0], coords[j][1] = x2, y2
        unit.goto(x2, y2)
        if x2 <= -365 or x2 >= 365:
            speeds[j][0] = -vx
        if y2 <= -300 or y2 >= 300:
            speeds[j][1] = -vy