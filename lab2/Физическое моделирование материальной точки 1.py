import turtle as tl
from math import sin, cos


tl.shape('circle')
v = 80
al = 3.14 / 3
tl.goto(380, 0)
x, y = -380, 0
dt = 0.1
ay = -10
ko = 0.9
kv = 0.0002
vx = v * cos(al)
vy = v * sin(al)
for i in range(1000):
    tl.goto(x, y)
    x += vx * dt
    y += vy * dt + ay * dt ** 2 / 2
    vx -= kv * vx ** 2
    vy += ay * dt
    if vy >= 0:
        vy -= kv * vy ** 2
    else:
        vy += kv * vy ** 2
    if y <= 0:
        vy = -vy * ko
        vx = vx * ko