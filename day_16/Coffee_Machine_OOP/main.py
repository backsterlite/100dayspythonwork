from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
turn_off = False

while not turn_off:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        turn_off = True
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


