#########################      Coffee Machine Project     ##############################

from machine_config import MENU, resources

money = 0

# Function to print a report of all resources and money available
def report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${money}')

# Function to check if there are sufficient ingredients to make the chosen coffee
def is_ingredients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process the coins inserted by the user and calculate the total payment
def process_coins():
    print("Please insert coins.")
    number_of_quarters = int(input("How many quarters?: "))
    number_of_dimes = int(input("How many dimes?: "))
    number_of_nickels = int(input("How many nickels?: "))
    number_of_pennies = int(input("How many pennies?: "))
    
    payment = 0.25 * number_of_quarters + 0.1 * number_of_dimes + 0.05 * number_of_nickels + 0.01 * number_of_pennies
    return payment

# Function to check if the transaction is successful based on the payment and cost of the coffee
def is_successful_transaction(payment, coffee_choice):
    global money
    cost = MENU[coffee_choice]["cost"]
    
    if payment >= cost:
        money += cost
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee by deducting the required ingredients from resources
def make_coffee(coffee_name):
    for ingredient in MENU[coffee_name]["ingredients"]:
        resources[ingredient] -= MENU[coffee_name]["ingredients"][ingredient]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")

# Main function to run the coffee machine
def run_machine():
    is_on = True
    while is_on:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        
        if coffee_choice == "report":
            report()
        elif coffee_choice == "off":
            is_on = False
        else:
            if is_ingredients_sufficient(MENU[coffee_choice]["ingredients"]):
                payment = process_coins()
                
                if is_successful_transaction(payment, coffee_choice):
                    make_coffee(coffee_choice)

# start running the coffee machine 
run_machine()
