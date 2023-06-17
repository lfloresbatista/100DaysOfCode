import turtle
import pandas
from state_pos import StateLocation

state_loc = StateLocation()
screen = turtle.Screen()
screen.title("Panama States Game")
screen.setup(width=800, height=500)
image = "panama_blank_map.gif"
screen.addshape(image)
turtle.shape(image)
user_score = 0
user_attempts = 0
corrected_guess = []

game_on = True

while game_on:
    user_guess = turtle.textinput(title=f"{user_score}/15 States Correct",
                                  prompt="What's is another state name?").title()
    user_attempts += 1
    if user_guess == "Exit":
        break
    if user_guess in state_loc.state_name.to_list():
        user_score += 1
        state_loc.show_location(user_guess)
        corrected_guess.append(user_guess)
    if user_score == 15:
        state_loc.game_over_win()
        game_on = False
    if user_attempts > 15:
        state_loc.game_over_lose()
        game_on = False
    print(corrected_guess)

corrected_guess_dict = { "Missing states": [] }

for state_miss in state_loc.state_name.to_list():
    if state_miss not in corrected_guess:
        corrected_guess_dict["Missing states"].append(state_miss)

states_to_learn = pandas.DataFrame(corrected_guess_dict)
states_to_learn.to_csv("states_to_learn.csv")