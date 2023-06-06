from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 70, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.update_sc()

    def update_sc(self):
        self.goto(-100, 190)
        self.write(arg=self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 190)
        self.write(arg=self.r_score, align=ALIGN, font=FONT)

    def new_score_l(self):
        self.clear()
        self.l_score += 1
        self.update_sc()

    def new_score_r(self):
        self.clear()
        self.r_score += 1
        self.update_sc()
