from turtle import Turtle, Screen
from data import color_list
import random

hp = Turtle()
screen = Screen()
screen.colormode(255)
# hp.pencolor(random.choice(color_list))
x = -300
y = -200
hp.speed("fastest")
hp.hideturtle()
hp.up()
hp.setpos(x, y)

for _ in range(10):
    for _ in range(10):
        hp.dot(20, random.choice(color_list))
        hp.fd(50)
        y += 5
    hp.setpos(x, y)

screen.exitonclick()

# TODO 10 x 10
# todo size=20 space=50
