import turtle as tl
from random import random, randint


tl.shape('turtle')
for i in range(100):
    tl.forward(randint(1, 100))
    tl.right(randint(-180, 180))