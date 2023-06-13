from turtle import Turtle
from data_color import color_list
import random

CAR_SPEED = 5


class Car:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 2:
            car = Turtle()
            car.up()
            car.shape("square")
            new_color = random.choice(color_list)
            car.color(new_color)
            car.resizemode("user")
            car.shapesize(1, 2)
            car.seth(180)
            new_y = random.randint(- 250, 250)
            car.goto(300, new_y)
            self.all_cars.append(car)


    def car_move(self):
        for car in self.all_cars:
            car.fd(CAR_SPEED)


