# from turtle import  Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
#
# screen.listen()
#
# screen.onkey(key="Escape" , fun=move_forwards)
#
# screen.exitonclick()

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def circle():
    tim.right(10)
    tim.forward(5)
tim.speed("fastest")
screen.listen()
screen.onkey(key="w", fun=move_forwards)  # Fixed key name
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.onkey(key="m"or"n", fun=circle)

screen.exitonclick()
