from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(height=400, width=400)
user_bet = screen.textinput("Turtle Race", "Wich turtule you think it will win?: ").lower()
all_tims = []
#TIMS LISTS
tims_colors = ["blue", "green", "yellow", "orange", "red"]
tims_pos_y = [0, 40, 80, -40, -80]


for n in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.up()
    tim.color(tims_colors[n])
    tim.goto(x=-180, y=tims_pos_y[n])
    all_tims.append(tim)

if user_bet:
    race_on = True

while race_on:
    for tim in all_tims:
        if tim.xcor() > 180:
            race_on = False
            win_color = tim.pencolor()
            if win_color == user_bet:
                print(f"Congrats your {user_bet.title()}'s Tim has Won!")
            else:
                print(f"Sorry your lose, the winner is the {win_color.title()}'s Tim")
        random_dis = random.randint(0,3)
        tim.fd(random_dis)
