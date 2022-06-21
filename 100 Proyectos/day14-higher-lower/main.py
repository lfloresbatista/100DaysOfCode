import random
from art import logo, vs
from game_data import data
from replit import clear


user_score = 0
game_over = False
next_A = {}
while not game_over:
    if user_score == 0:
        A = random.choice(data)
        B = random.choice(data)
        if A == B:
            A = random.choice(data)
    else:
        A = next_A
        B = random.choice(data)
    if B == A:
        B = random.choice(data)
    
                
    print(logo)   
    print("Compare A: " + A["name"] + ", a " + A["description"] + ", from " + A["country"])
    print(vs)
    print("Against B: " + B["name"] + ", a " + B["description"] + ", from " + B["country"])
 
    user_choice = input("Who has more followers? type 'A' or 'B': ").lower()

    if user_choice == "a" and A["follower_count"] > B["follower_count"]:
        user_score += 1
        clear()
        print(f"You're Right! Current Score: {user_score}")
        next_A = B
        game_over = False
    elif user_choice == "b" and B["follower_count"] > A["follower_count"]:
        user_score += 1
        clear()
        print(f"You're Right! Current Score: {user_score}")
        next_A = B
        game_over = False
    else:
        clear()
        print(logo)
        print(f"Sorry you lose. Final Score: {user_score}")
        game_over = True
