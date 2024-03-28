from turtle import Turtle
from turtle import mainloop

# print(dir(Turtle))
def square(size, t):
    for i in range(4):
        t.fd(size)
        t.rt(90)

def triangle(size, t):
    for i in range(3):
        t.fd(size)
        t.rt(120)


