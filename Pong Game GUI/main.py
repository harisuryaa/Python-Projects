from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

score= Score()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game GUI")
screen.tracer(0)

paddle = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_positon()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_positon()
        score.increase_r()

    if score.l_score > 2 or score.r_score > 2:
        score.game_over()
        game_is_on =False

screen.exitonclick()
