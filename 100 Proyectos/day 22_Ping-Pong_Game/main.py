from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping-Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(r_paddle.pad_up, "Up")
screen.onkey(r_paddle.pad_down, "Down")
screen.onkey(l_paddle.pad_up, "w")
screen.onkey(l_paddle.pad_down, "s")



game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < - 270:
        ball.bounce_y()

    #dteect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()


    #Left Score
    if ball.xcor() > 380:
        scoreboard.new_score_l()
        ball.reset_ball()

    #iRght Score
    if ball.xcor() < -380:
        scoreboard.new_score_r()
        ball.reset_ball()


screen.exitonclick()

