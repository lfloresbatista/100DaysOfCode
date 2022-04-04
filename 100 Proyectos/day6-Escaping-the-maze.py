#Hi it took me like 3 hours, but without watching the solution, I find a way who resolved all the three problems, Whem I test this I was a begginer, and wors. Thanks for watching
#there is my code

def right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():    
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_on_right() and front_is_clear():
        move()
        if wall_on_right() and front_is_clear():
            turn_left()
    elif wall_in_front() and right_is_clear():
        right()
    elif right_is_clear() and front_is_clear():
       move()
    else:
        move()
