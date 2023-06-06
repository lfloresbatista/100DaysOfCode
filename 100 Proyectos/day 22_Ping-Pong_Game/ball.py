from turtle import Turtle
TOP_Y = 590
BALL_SPEED_CONST = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.ball_max_speed = 0.016

    def move(self):
        start_x = self.xcor() + self.x_move
        start_y = self.ycor() + self.y_move
        self.goto(start_x, start_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed -= 0.02
        if self.ball_speed < self.ball_max_speed:
            self.ball_speed = self.ball_max_speed

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = BALL_SPEED_CONST


