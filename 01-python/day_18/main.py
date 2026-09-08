# from turtle import  Turtle ,Screen
#
# ti = Turtle()
# ti.shape("turtle")
# ti.color("red")
# ti.forward(100)
# ti.left(120)
# ti.forward(100)
# ti.left(120)
# ti.forward(100)
import random
# from turtle import  Turtle ,Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

#
# for i in range(1,5):
#     tim.forward(100)
#     tim.left(90)

# import heroes
# print(heroes.gen())

#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# for side in range(3,11):
#     tim.color(random.choice(colours))
#     angle = 360/side
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(angle)






# screen = Screen()
# screen.exitonclick()

import  turtle as t
import  random


tim = t.Turtle

# colour = ["CornflowerBlue","DarkOrchid","IndianRed", "DeepSkyBlue" , "LightSeaGreen" , "Wheat","SlateGray", "SeaGreen"   ]

directions = [0,90,180,270]


for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
screen = t.Screen()
screen.exitonclick()
