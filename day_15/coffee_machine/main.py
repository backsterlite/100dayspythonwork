import data

QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01


def get_drink_obj(drink_name):
    return data.MENU[drink_name]


def get_resources_obj():
    return data.resources


def coffee_machine_off(drink):
    exit(0)


def print_report(drink):
    for key in data.resources:
        if key == 'money':
            print(f"{key}: ${data.resources[key]}")
        else:
            print(f"{key}: {data.resources[key]}")
    restart_coffee_machine()


def check_enough_resources(drink_name):
    drink = get_drink_obj(drink_name)
    not_enough_resource = ''
    if 'water' in drink['ingredients'].keys() and data.resources['water'] < drink['ingredients']['water']:
        not_enough_resource = 'water'
    elif 'milk' in drink['ingredients'].keys() and data.resources['milk'] < drink['ingredients']['milk']:
        not_enough_resource = 'milk'
    elif 'coffee' in drink['ingredients'].keys() and data.resources['coffee'] < drink['ingredients']['coffee']:
        not_enough_resource = 'coffee'
    if bool(not_enough_resource):
        print(f"Sorry there is not enough {not_enough_resource}.")
        restart_coffee_machine()


def process_coins(drink_name):
    drink = get_drink_obj(drink_name)
    print("Please insert coins.")
    money = float(input("how many quarters?: ")) * QUARTERS
    money += float(input("how many dimes?: ")) * DIMES
    money += float(input("how many nickles?: ")) * NICKLES
    money += float(input("how many pennies?: ")) * PENNIES
    money = round(money, 2)
    if money < drink['cost']:
        print('Sorry that\'s not enough money. Money refunded.')
        restart_coffee_machine()
    else:
        resources = get_resources_obj()
        resources['money'] += drink['cost']
        change = money - drink['cost']
        print(f"Here is ${change} in change.")


def decrease_resources(drink_name):
    drink = get_drink_obj(drink_name)
    resources = get_resources_obj()
    for key in resources.keys():
        if key in drink['ingredients']:
            resources[key] -= drink['ingredients'][key]


def make_drink(drink):
    drink_obj = get_drink_obj(drink)
    check_enough_resources(drink)
    print(f"{drink} cost is a ${drink_obj['cost']}")
    process_coins(drink)
    decrease_resources(drink)
    print(f"Here is your {drink} ☕️. Enjoy!")
    restart_coffee_machine()


def restart_coffee_machine():
    start_coffee_machine()


machine_variants = {
    "espresso":   make_drink,
    "latte":      make_drink,
    "cappuccino": make_drink,
    "report":     print_report,
    "off":        coffee_machine_off,

}


def start_coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    try:
        machine_variants[choice](choice)
    except Exception:
        print("You type wrong parameter. Try again")
        start_coffee_machine()


start_coffee_machine()
