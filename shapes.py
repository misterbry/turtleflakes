from turtle import Turtle
from turtle import mainloop

# print(dir(Turtle))
t = Turtle()
def square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)

def triangle(size):
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.rt(120)
    t.end_fill()
    
triangle(100)
# square(100)
mainloop()
