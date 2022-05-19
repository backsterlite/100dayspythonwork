from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_extra_card(user):
    new_card = random.choice(cards)
    if new_card == 11 and sum(cards) + new_card > 21:
        new_card = 1
    user.append(new_card)
    return user


def is_need_extra_card(dealer):
    return sum(dealer) < 17


def is_blackjack(cards):
    return (11 in cards) and (10 in cards)


def get_game_result(user, dealer):
    if sum(user) > 21:
        return 'You are owerflow. You lose'
    elif (sum(user) == sum(dealer)) and (is_blackjack(user) and is_blackjack(dealer)):
        return 'Is a blackjack draw. You win'
    elif sum(user) == sum(dealer):
        return 'Is a draw. You lose'
    elif sum(user) < sum(dealer):
        return 'You hand is too litle. You lose'
    elif sum(user) > sum(dealer):
        return 'Your hand better. You win'


def cards_deal():
    user_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)
    return user_cards, dealer_cards


def is_start_new_game():
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'


def game():
    open_cards = False
    os.system('clear')
    print(logo)
    user_cards, dealer_cards = cards_deal()
    while not open_cards:
        if sum(user_cards) <= 21:
            print(
                f'\tYour cards: {user_cards}, current score: {sum(user_cards)}\n\tComputer\'s first card: {dealer_cards[0]}')
            user_get_extra_card = input("Type 'y' to get another card, type 'n' to pass:")

            if user_get_extra_card == 'y':
                user_cards = get_extra_card(user_cards)
                if is_need_extra_card(dealer_cards):
                    dealer_cards = get_extra_card(dealer_cards)
            else:
                while is_need_extra_card(dealer_cards):
                    dealer_cards = get_extra_card(dealer_cards)
                open_cards = True

        else:
            open_cards = True
    print(
        f'\tYour final hand: {user_cards}, final score: {sum(user_cards)}\n\tComputer\'s final hand: {dealer_cards}, final score: {sum(dealer_cards)}')
    print(get_game_result(user_cards, dealer_cards))
    if is_start_new_game():
        game()


if is_start_new_game():
    game()
