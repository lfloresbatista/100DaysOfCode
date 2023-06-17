from turtle import Turtle
import pandas

ALIGN = "center"
FONT = ('Arial', 10, 'bold')


class StateLocation(Turtle):
    def __init__(self):
        self.states_location = pandas.read_csv("panama_states.csv")
        self.state_name = self.states_location.state
        self.state_x = self.states_location.x
        self.state_y = self.states_location.y
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.up()
        self.goto(0, 0)
        self.speed("slow")
        # self.show_location()

    def show_location(self, state):
        self.goto(self.state_x[self.state_name == state].iloc[0], self.state_y[self.state_name == state].iloc[0])
        self.write(arg=state, align=ALIGN, font=FONT)

    def game_over_lose(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="Im Sorry! you reached the maximum attempts", align=ALIGN, font=('Arial', 20, "bold"))

    def game_over_win(self):
        self.goto(0, 0)
        self.color("blue")
        self.write(arg="WAO!!! You are a Genius my friend.", align=ALIGN, font=('Arial', 20, "bold"))
