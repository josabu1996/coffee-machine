machine_status = True
service_status = True
WATER_CAP = 500
MILK_CAP = 500
COFFEE_CAP = 300
PASSWORD = "1234"
water = 500
milk = 500
coffee = 300
money = 0
balance = 0


def money_checker(coffee):
    global money
    global balance
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    money_received = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    if coffee == 'espresso':
        prize = 1.50
        if money_received < prize:
            print("Sorry that's not enough money. Money refunded.")
        else:
            balance = money_received - prize
            money += prize
            return money
    elif coffee == 'latte':
        prize = 2.50
        if money_received < prize:
            print("Sorry that's not enough money. Money refunded.")
        else:
            balance = money_received - prize
            money += prize
            return money
    elif coffee == 'Cappuccino':
        prize = 3.00
        if money_received < prize:
            print("Sorry that's not enough money. Money refunded.")
        else:
            balance = money_received - prize
            money += prize
            return money


def check_resource(s_status, coffee_type):
    global water
    global coffee
    global milk
    if not s_status:
        print("Machine already in Maintenance Mode.")
    else:
        if coffee_type == "espresso":
            if water < 50:
                print("Sorry there is not enough water.")
            elif coffee < 18:
                print("Sorry there is not enough coffee.")
            else:
                money = money_checker(coffee_type)
                water -= 50
                coffee -= 18
                if balance > 0:
                    print(f"Here is your balance ${round(balance, 2)} in change.")
                print(f"Here's your Espresso ☕ Enjoy!")
        elif coffee_type == "latte":
            if water < 200:
                print("Sorry there is not enough water.")
            elif coffee < 24:
                print("Sorry there is not enough coffee.")
            elif milk < 150:
                print("Sorry there is not enough milk.")
            else:
                money = money_checker(coffee_type)
                water -= 200
                coffee -= 24
                milk -= 150
                if balance > 0:
                    print(f"Here is your balance ${round(balance, 2)} in change.")
                print(f"Here is your Latte ☕ Enjoy!")
        elif coffee_type == "cappuccino":
            if water < 250:
                print("Sorry there is not enough water.")
            elif coffee < 24:
                print("Sorry there is not enough coffee.")
            elif milk < 100:
                print("Sorry there is not enough milk.")
            else:
                money = money_checker(coffee_type)
                water -= 250
                coffee -= 24
                milk -= 100
                if balance > 0:
                    print(f"Here is your balance ${round(balance, 2)} in change.")
                print(f"Here's your Cappuccino ☕ Enjoy!")


def prompt_off(s_status):
    if not s_status:
        print("Machine already in Maintenance Mode.")
    else:
        pwd_match = False
        while not pwd_match:
            pwd = input("Enter Admin password: ")
            if pwd == PASSWORD:
                pwd_match = True
                s_status = False
                print("Switching to Maintenance Mode.")
                return s_status
            else:
                print("Wrong password please try again.")


def prompt_resource(s_status, coffee_type):
    if not s_status:
        print("Machine currently in Maintenance Mode. We will be back soon!")
    else:
        check_resource(s_status, coffee_type)


def prompt_report():
    print(f"\nResource Availability:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n")


while machine_status:
    input_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if input_prompt == "off":
        service_status = prompt_off(service_status)
    elif input_prompt == "espresso" or input_prompt == "latte" or input_prompt == "cappuccino":
        prompt_resource(service_status, input_prompt)
    elif input_prompt == "report":
        prompt_report()
