from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.seth(90)

    def move(self):
        self.y_move = self.ycor() + 10
        self.goto(0, self.y_move)

    def restart_player(self):
        self.goto(STARTING_POSITION)

