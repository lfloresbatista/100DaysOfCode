from turtle import Turtle

ALIGN = "left"
FONT = ('Courier', 16, 'bold')



class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.up()
        self.curr_level = 1
        self.update_sc()

    def update_sc(self):
        self.goto(-280, 250)
        self.write(arg=f"LEVEL: {self.curr_level}", align=ALIGN, font=FONT)

    def new_level(self):
        self.clear()
        self.curr_level += 1
        self.update_sc()

    def game_over(self):
        self.up()
        self.goto(0, 0)
        self.color("red")
        self.write(arg=f"GAME OVER", align="center", font=FONT)
        self.goto(0, -20)
        self.write(arg=f"YOUR REACHED THE {self.curr_level} LEVEL", align="center", font=FONT)