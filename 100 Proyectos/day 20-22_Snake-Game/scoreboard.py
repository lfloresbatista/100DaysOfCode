from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 13, 'bold')
DEFAULT_POS = (0, 275)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(DEFAULT_POS)
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGN, font=FONT)
    def new_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

