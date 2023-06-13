from turtle import Screen
from player import Player
from levelboard import LevelBoard
from cars import Car
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)
screen.colormode(255)

player = Player()
level = LevelBoard()
cars = Car()

screen.onkey(player.move, "Up")

car_loop = 1
game_on = True
sleep_default = 0.2
max_speed = 0.001
while game_on:
    screen.update()
    time.sleep(sleep_default)
    cars.create_car()
    cars.car_move()
    if player.ycor() > 280:
        player.restart_player()
        level.new_level()
        sleep_default -= 0.03
        if sleep_default <= 0.01:
            sleep_default = max_speed
    for car_pos in cars.all_cars:
        if car_pos.distance(player) < 20:
            level.game_over()
            game_on = False


screen.exitonclick()