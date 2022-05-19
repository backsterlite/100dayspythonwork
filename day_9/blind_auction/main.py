import os
from art import logo

# HINT: You can call clear() to clear the output in the console.
auction_exit = False
users = []
winner_name = ''
winner_bid = 0
print(logo)
print("Welcome to the secret auction program.")

while not auction_exit:
    user_name = input('What is your name? ')
    user_bid = int(input('What is your bid? $'))
    users.append({"name": user_name, "bid": user_bid})
    print(users)
    if input("Are there any others bidders? Type 'yes' or 'no'") == 'no':
        auction_exit = True
    os.system('clear')

for user in users:
    if user['bid'] > winner_bid:
        winner_name = user['name']
        winner_bid = user['bid']

print(f'The winner is {winner_name} with a bid of ${winner_bid}.')
