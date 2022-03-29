rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Bienvenidos al mundo de piedra, papel o tijeras by Luis")
user = int(input("Que eliges? Escribe 0 para piedra, 1 para papel, 2 para tijeras:\n"))
ai = random.randint(0,2)
#print user choice
if user == 0:
  print(rock)
elif user == 1:
  print(paper)
elif user == 2:
  print(scissors)
else:
  print("⛔ Lo siento la opcion que escogiste es incorrecta, intentalo de nuevo. ⛔")
#print computer choice
if ai == 0:
  print("La computadora eligio:\n" + rock)
elif ai == 1:
  print("La computadora eligio:\n" + paper)
else:
  print("La computadora eligio:\n" + scissors)
#print result
if user == 0 and ai == 2 or user == 2 and ai == 1 or user == 1 and ai == 0:
  print("🥳 🥳 🥳 Felicidades Ganaste la partida!")
elif ai == 0 and user == 2 or ai == 2 and user ==1 or ai == 1 and user == 0:
  print("🤡 🤡 🤡 Lo siento haz perdido la partida!")
else:
  print("🤖 🤖 🤖 Vaya vaya, seguro eres humano? intentalo de nuevo!")

print("Gracias por participar en mi juego, puedes compartir el link con tus amigos")
