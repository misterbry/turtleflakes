from turtle import Turtle
from turtle import tracer
from turtle import bye
from shapes import triangle as tri

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
    
def triflakes():
    # t1 = Turtle()
    # t2 = Turtle()
    # t3 = Turtle()
    # t4 = Turtle()

    # turtles = [t1, t2, t3, t4]
    turtles = [Turtle() for _ in range(4)]
    turtles[0].screen.listen()
    turtles[0].screen.onkey(bye, 'x')
    for turtle in turtles:
        turtle.penup()
    turtles[0].setpos(70, 70)
    turtles[1].setpos(70, -70)
    turtles[2].setpos(-70, -70)
    turtles[3].setpos(-70, 70)
    for turtle in turtles:
        turtle.pendown()
        turtle.speed(0)
        for i in range(24):
            tri(20, turtle)
            turtle.rt(15)
