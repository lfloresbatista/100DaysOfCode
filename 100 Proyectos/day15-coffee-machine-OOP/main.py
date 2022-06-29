from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm_menu = Menu()
cm_barista = CoffeeMaker()
cm_money = MoneyMachine()
is_on = True

#TODO: 1 Promp user what would you like?
while is_on:
    user_choice = input(f"What would you like? ({cm_menu.get_items()}) : ").lower()
    #TODO: 2 Turn off the MAchine
    if user_choice == "off":
        print("Thanks!")
        is_on = False
    #TODO: 3 Print a report
    elif user_choice == "report":
        cm_barista.report()
        cm_money.report()
    else:
        drink = cm_menu.find_drink(user_choice)
        if cm_barista.is_resource_sufficient(drink):
            if cm_money.make_payment(drink.cost):
                cm_barista.make_coffee(drink)
