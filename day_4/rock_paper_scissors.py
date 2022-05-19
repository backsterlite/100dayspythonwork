import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ROCK = 0
PAPER = 1
SCISSORS = 2
variants = [rock, paper, scissors]
print('Start the game by asking the player:')
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer = random.randint(0, 2)
print(variants[user])
print(f'computer:\n{variants[computer]}')
if user == computer:
    print("You are tie")
elif user == ROCK and computer == SCISSORS \
        or user == PAPER and computer == ROCK \
        or user == SCISSORS and computer == PAPER:
    print("You win!)")
else:
    print('You lose!(')
