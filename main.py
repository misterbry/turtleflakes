# https://docs.python.org/3/library/turtle.html
from turtle import mainloop
from flakes import mr_bryan_flake as mrb
from flakes import triflakes
from turtle import Turtle

def main():
    print(dir(Turtle))
    # mrb()
    triflakes()
    mainloop()

if __name__ == '__main__':
    main()
