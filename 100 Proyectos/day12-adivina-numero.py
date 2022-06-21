
import random
#from art import logo

logo = """
              _ _       _                           _ _       _                 _            
     /\      | (_)     (_)                 /\      | (_)     (_)               | |           
    /  \   __| |___   ___ _ __   __ _     /  \   __| |___   ___ _ __   __ _  __| | ___  _ __ 
   / /\ \ / _` | \ \ / / | '_ \ / _` |   / /\ \ / _` | \ \ / / | '_ \ / _` |/ _` |/ _ \| '__|
  / ____ \ (_| | |\ V /| | | | | (_| |  / ____ \ (_| | |\ V /| | | | | (_| | (_| | (_) | |   
 /_/    \_\__,_|_| \_/ |_|_| |_|\__,_| /_/    \_\__,_|_| \_/ |_|_| |_|\__,_|\__,_|\___/|_|   
                                                                                             
                                                               
"""

print(logo)


NUMBER_TO_GUESS = random.randint(1, 100)
attemps = 0
game_over = False

def user_level():
    """Esta funcion es para definir la cantidad de intentos del juego."""
    global attemps
    if level_choose == "facil":
        attemps = 10
    elif level_choose == "dificil":
        attemps = 5
    print(f"Excelente! Tienes {attemps} intentos, para adivinar el numero")

def attemps_zero():
    if attemps == 0:
        if user_guess < NUMBER_TO_GUESS:
            print("Muy Bajo.")
            print("Te quedaste sin intentos. Pediste")
            game_over = True
            return game_over
        elif user_guess > NUMBER_TO_GUESS:
            print("Muy Alto.")
            print("Te quedaste sin intentos. Pediste")
            game_over = True
            return game_over        
    else:
        game_over = False
        return game_over


print("Bienvenido al juego de Adivinando el numero")
print("Estoy pensando en un numero entre 1 y 100.")


level_choose = input("Elige la dificultad. Escribre 'facil' o 'dificil': ").lower()

user_level()

while not game_over:
    user_guess = int(input("Adivina el numero: "))
    if user_guess > NUMBER_TO_GUESS:
        attemps -= 1
        print("Muy Alto.")
        print("Adivina de nuevo")
        print(f"Te quedan {attemps} intentos para adivinar el numero:")
        game_over = attemps_zero()                      
    elif user_guess < NUMBER_TO_GUESS:
        attemps -= 1
        print("Muy Bajo.")
        print("Adivina de nuevo")
        print(f"Te quedan {attemps} intentos para adivinar el numero:")
        game_over = attemps_zero()
    elif user_guess == NUMBER_TO_GUESS:
        print(f"Excelente! la respuesta era : {NUMBER_TO_GUESS}")
        game_over = True
        
