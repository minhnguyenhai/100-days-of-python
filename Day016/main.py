from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start_coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    
    is_on = True
    while is_on:
        user_choice = input(f"What would you like? ({menu.get_items()})")
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice == "off":
            is_on = False
        else:
            ordered_drink = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink.cost):
                coffee_maker.make_coffee(ordered_drink)
                    

if __name__ == "__main__":
    start_coffee_machine()