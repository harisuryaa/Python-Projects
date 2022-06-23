from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveforward():
    tim.forward(10)
def move_back():
    tim.back(10)
def turn_right():
    tim.right(10)
def turn_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(moveforward, "w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()