print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenidos a la busqueda del tesoro by Luis")
print("Tu mision es exontrar el tesoro escondido")

left_or_right = input("Estar por elegir un camino, Cual camino eliges? Escribe: \"derecha\" o \"izquierda\"\n")
left_or_right = left_or_right.lower()

if left_or_right == "derecha":
  print("Caiste en un juego.\nFin de la Partida.")
elif left_or_right == "izquierda":
  swim_or_wait = input("Perfecto!!! Ahora te encuentras frente a una isla, que deseas hacer? Escribe: \"nadar\" o \"esperar\"\n")
  swim_or_wait = swim_or_wait.lower()
  if swim_or_wait == "nadar":
    print("Noooo!!! haz sido atacado por un Megalodon.\nFin de la partida.")
  elif swim_or_wait == "esperar":
    doors = input("Excelente eleccion!! un bote te ha recogido y haz logrado cruzar a la isla, pero, Debes ingresar por una de sus tres puertas. Escribe \"azul\" o \"amarillo\" o \"roja\"\n")
    doors = doors.lower()
    if doors == "roja" or doors == "roja":
      print("Los siento. Haz sido carbonizado con fuego\nFin de la partida")
    elif doors == "azul":
      print("Uppss. Haz sido comido por bestias salvajes.\nFin de la partida.")
    elif doors == "amarillo" or "amarilla":
      print("Felicidades haz encontrado el tesoro.\nHaz ganado este juego.\nGracias por participar.")
    else:
      print("Opcion no encontrada.\nFin de la partida.")
  else:
    print("Opcion no encontrada.\nFin de la partida.")
else:
  print("Opcion no encontrada.\nFin de la partida.")
  
