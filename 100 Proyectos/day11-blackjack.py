import random
#from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 8, 10, 10, 10, 10]


def bj_status():
    if pc_score == 21:
        print(f"Lo siento, la casa gana con BlackJack, estas fueron las cartas: {pc_cards}")
        game_over = True
        return game_over
    elif user_score == 21:
        print(f"BlackJack!, Felicidades haz ganado, estas fueron tus cartas: {user_cards}")
        game_over = True
        return game_over
    else:
        game_over = False
        return game_over

    
def winner():
    print(f"    Tus ultimas cartas son: {user_cards}, tu puntaje final es: {user_score}\n    Las ultimas cartas de la casa son: {pc_cards}, y el puntaje final de la casa es: {pc_score}")
    if user_score > 21:
        print("Perdiste. Te haz pasado de 21.")
        game_over = True
        return game_over
    elif pc_score > 21:
        print("Ganaste. La casa se ha pasado de 21.")
        game_over = True
        return game_over
    elif user_score > pc_score:
        print("Ganaste")
        game_over = True
        return game_over
    elif pc_score > user_score:
        print("Perdiste, la casa gana.")
        game_over = True
        return game_over
    elif user_score == pc_score:
        print("Empate.")
        game_over = True
        return game_over
    else:
        game_over = False
        return game_over

def blackjack():
    play = input("Desearias jugar un juego de BlackJack? Escribe 'si' ó 'no': ").lower()
    return play


while blackjack() == "si":
    #clear() ///Replit function to clear the screen
    print(logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    user_score = sum(user_cards)
    pc_cards = [random.choice(cards), random.choice(cards)]
    pc_score = sum(pc_cards)
    print(f"    Tus cartas son: {user_cards}, tu puntaje actual: {user_score}\n    La primera carta de la casa es: {pc_cards[0]}")
    game_over = bj_status()
    
    while not game_over:
        more_card = input("Escribe 'si' para pedir otra carta, ó escribe 'no' para pasar: ").lower()
        if more_card == "si":
            next_card = random.choice(cards)
            user_cards.append(next_card)
            user_score += next_card
            print(f"    Tus cartas son: {user_cards}, tu puntaje actual: {user_score}\n    La primera carta de la casa es: {pc_cards[0]}")
        if user_score >= 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                user_score = sum(user_cards)
                print(f"Tienes una A y se ha reemplazado 11 por 1 tus nuevas cartas son {user_cards}, tu nuevo puntaje es: {user_score}")
                if user_score >= 21:
                    game_over = winner()
            else:
                game_over = winner()
        elif pc_score <= 16:
            next_card_pc = random.choice(cards)
            pc_cards.append(next_card_pc)
            pc_score += next_card_pc
        if pc_score >= 21:
            if 11 in user_cards:
                pc_cards.remove(11)
                pc_cards.append(1)
                pc_score = sum(pc_cards)
                print("La casa tiene una A, se ha reemplazado el 11 por 1")
                if pc_score >= 21:
                    game_over = winner()
            else:
                game_over = winner()
        elif more_card == "no":
            game_over = winner()


