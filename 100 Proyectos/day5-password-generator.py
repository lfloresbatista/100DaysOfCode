#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido al generador de contrasenas by Luis")
nr_letters= int(input("Cuantas letras quieres en tu contrasena?\n")) 
nr_symbols = int(input(f"Cuantos simbolos te gustarian?\n"))
nr_numbers = int(input(f"Cuantos numeros quieres?\n"))

password_lst =  []
final_pass = ""
for ch in range(1,nr_letters + 1):
  password_lst += [random.choice(letters)]
for ch in range(1,nr_symbols + 1):
  password_lst += [random.choice(symbols)]
for ch in range(1,nr_numbers + 1):
  password_lst += [random.choice(numbers)]
  random.shuffle(password_lst)
for passwd in password_lst:
  final_pass += passwd
print(f"Tu contrasena es: {final_pass}")
