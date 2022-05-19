from art import logo
import os


def add(num1, num2):
    """return sum of two numbers"""
    return num1 + num2


def sub(num1, num2):
    """return substract of two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """return multiply of two numbers"""
    return num1 * num2


def div(num1, num2):
    """return divide of two numbers"""
    return num1 / num2


calculate = {'+': add, '-': sub, '*': multiply, '/': div}


def calculator():
    exit_calculate = False
    print(logo)
    num1 = float(input('What is the first number?: '))
    while not exit_calculate:
        for operator in calculate:
            print(operator)
        operator = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))
        last_result = calculate[operator](num1, num2)
        print(f'{num1} {operator} {num2} = {last_result}')
        next_action = input(
            f"Type 'y' to continue calculating with {last_result}, or type 'n' to start a new calculation or type 'f' for finishing calculating:")
        if next_action == 'y':
            num1 = last_result
        elif next_action == 'n':
            os.system('clear')
            calculator()
        elif next_action == 'f':
            exit_calculate = True


calculator()
