# https://docs.python.org/3/library/turtle.html

from turtle import Turtle
from turtle import mainloop
from random import random

pat = Turtle()

# Function Definitions

def my_turtleflake():
    pat.speed(15)
    pat.pencolor("red")
    pat.screen.colormode(255)
    pat.fillcolor(100, 0, 0)
    pat.screen.title("****** Turtle Flakes ******")
    pat.screen.bgcolor(0, 0, 100)

    for i in range(24):
        pat.begin_fill()
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(135)
        pat.end_fill()
        
    for i in range(3):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
        pat.penup()
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(135)
        pat.pendown()
        
    pat.hideturtle()
    
mainloop()
