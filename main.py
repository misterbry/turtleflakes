import turtle

print(dir(turtle))

pat = turtle.Turtle()

for i in range(2):
    pat.forward(100)
    pat.right(60)
    pat.forward(100)
    pat.right(120)

turtle.mainloop()
