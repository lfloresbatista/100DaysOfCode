from turtle import Turtle

RIGHT = (350, 0)
LEFT = (-350, 0)



class Paddle(Turtle):
    def __init__(self, position):
        """Position str: right or left"""
        super().__init__()
        self.up()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(5, 1)
        if position == "left":
            self.goto(LEFT)
        elif position == "right":
            self.goto(RIGHT)
        else:
            pass


    def pad_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def pad_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
