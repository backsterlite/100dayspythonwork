# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def get_lives_by_difficult(difficult):
    if difficult == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def decriment_lives(lives):
    return lives - 1


def lose_way(correct_number, guessed_number):
    if guessed_number > correct_number:
        print('Too high')
    else:
        print('Too low')


def welcome():
    print(logo)
    print('Welcome to the Number Guessing Game!\n\
          I\'m thinking of a number between 1 and 100.')
    return input("Choose a difficulty. Type 'easy' or 'hard':")


gameover = False
my_number = random.randint(1, 100)
difficult = welcome()
print(f'guessed number is: {my_number}')
lives = get_lives_by_difficult(difficult)
print(f"You have {lives} attempts remaining to guess the number.")
while not gameover:
    guess_number = int(input('Make a guess: '))
    if guess_number == my_number:
        gameover = True
        print(f"You got it! The answer was {my_number}.")
    else:
        lose_way(my_number, guess_number)
        lives = decriment_lives(lives)
        if lives == 0:
            gameover = True
            print('You\'ve run out of guesses, you lose.')
        else:
            print('Guess again.')
            print(f"You have {lives} attempts remaining to guess the number.")
