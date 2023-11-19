import turtle as t
import random
t.colormode(255)
color=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim=t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)
# tim.dot(20,"blue")
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
numbers_of_dots=100

for dots in range(1,numbers_of_dots+1):
    tim.dot(20, random.choice(color))
    tim.forward(50)

    if dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen=t.Screen()
screen.exitonclick()

