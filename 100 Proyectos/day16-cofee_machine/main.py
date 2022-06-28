


from menu_dic import MENU, resources


turn_off = False
profit = 0

#Functions
def inventory_satus(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Lo sentimos no tenemos suficiente {item}, para preparar su bebida")
            return False
    return True


def coins():
    total = int(input("Cuantas monedas de 50 centavos?: ")) * 0.50
    total += int(input("Cuantos denominaciones de 1$?: ")) * 1.0
    total += int(input("Cuantas monedas de 25 centavos?: ")) * 0.25
    total += int(input("Cuantas monedas de 10 centavos?: ")) * 0.10
    total += int(input("Cuantas monedas de 5 centavos?: ")) * 0.05
    total += int(input("Cuantas monedas de 1 centavo?: ")) * 0.01
    return total


def transaction_status(money, cost):
    if money >= cost:
        global profit
        change = money - cost
        profit += cost
        print(f"Gracias, Aqui esta su cambio ${change:.2F}.")
        return True
    else:
        print(f"Lo siento la cantidad de ${money:.2F} no es suficiente")
        return False

def barista(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Su {drink_name} esta listo, Disfrutelo")

while not turn_off:
    user_choice = input("Que le gustaria? (espresso/latte/capuccino): ").lower()
    if user_choice == "off":
        print("Gracias por utlizar nuestro Coffe Machine.")
        turn_off = True
    elif user_choice == "report":
        print(f"Agua: {resources['water']}ml.")
        print(f"Leche: {resources['milk']}ml.")
        print(f"Cafe: {resources['coffee']}g.")
        print(f"Ganancias: ${profit}")
    else:
        drink = MENU[user_choice]
        if inventory_satus(drink["ingredients"]):
            payment = coins()
            if transaction_status(payment, drink['cost']):
                barista(user_choice,drink["ingredients"])





