import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
extracted_color=[(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim. forward(250)
tim.setheading(0)

def forward_line():
    for i in range (10):
        tim.dot(20, random.choice(extracted_color))
        tim.forward(50)
for j in range(5):
    forward_line()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)




my_screen=turtle.Screen()
my_screen.exitonclick()