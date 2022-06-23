from turtle import Turtle, Screen
import random

timme_the_turtle = Turtle()

colours= ["brown","orange red", "spring green","medium slate blue","light coral","linen","navy","deep sky blue","light cyan","aquamarine","light green","magenta","orange"]
def shape(n):
    for _ in range(n):
        timme_the_turtle.right(360/n)
        timme_the_turtle.forward(100)
m=0
for n in range(3, 11):
    timme_the_turtle.color(random.choice(colours))
    shape(n)

screen = Screen()
screen.exitonclick()
