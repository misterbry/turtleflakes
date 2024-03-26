from turtle import Turtle
from turtle import tracer
from turtle import bye

def mr_bryan_flake():
    pat = Turtle()
    tracer(0, 0)
    pat.hideturtle()
    pat.screen.screensize(400, 400)
    pat.screen.colormode(255)    
    pat.speed(0)
    pat.pencolor("red")
    pat.fillcolor(100, 0, 0)
    pat.screen.title("****** Turtle Flakes ******")
    pat.screen.bgcolor(0, 0, 100)
    pat.screen.listen()
    pat.screen.onkey(bye, 'x')

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
    
