from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)
print("Bienvenidos al programa de Subasta Secreta.")

secret_auction = {}
def name_bid():
    name = input("Cual es tu nombre?: ")
    bid = int(input("Cual es tu oferta?: $"))
    secret_auction[name] = bid

continued = True
while continued:
    name_bid()
    continued = input("Hay algun otro ofertador? Escribe 'Si' o 'No'.\n").lower()
    if continued == "si":
        clear()
    if continued == "no":
        continued = False

#EASY WAY
# winner = max(secret_auction, key= secret_auction.get)
# print(f"EL ganador de la subaste es: {winner}, con una oferta de: ${secret_auction[winner]}")
        
#SAYAYIN WAY        
bid_list = []
max_bid = 0
for key in secret_auction:
    bid_list.append(secret_auction[key])
    max_bid = max(bid_list)

for bider in secret_auction:
    if max_bid == secret_auction[bider]:
        print(f"El ganador de la subasta es: {bider}, con una oferta de ${max_bid}.")
