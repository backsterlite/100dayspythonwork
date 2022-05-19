import os
import art
import game_data
import random

game_over = False
last_save_target = {}
player_score = 0


def get_targets():
    last_index = len(game_data.data) - 1
    index_a = random.randint(0, last_index)
    index_b = random.randint(0, last_index)
    while index_a == index_b:
        index_b = random.randint(0, last_index)

    print(f"index_a = {index_a}")
    print(f"index_b = {index_b}")
    target_a = last_save_target if bool(last_save_target) else game_data.data[index_a]
    target_b = game_data.data[index_b]
    return target_a, target_b


def print_new_round_info(target_a, target_b, score):
    print(art.logo)
    if score != 0:
        print(f'You\'re right! Current score: {score}.')
    print(f"Compare A: {target_a['name']}, a {target_a['description']}, from {target_a['country']}.")
    print(art.vs)
    print(f"Against B: {target_b['name']}, a {target_b['description']}, from {target_b['country']}.")


def get_round_result(target_a, target_b, choice):
    if choice == 'A' and target_a['follower_count'] > target_b['follower_count']:
        return True, target_a
    elif choice == 'B' and target_a['follower_count'] < target_b['follower_count']:
        return True, target_b
    return False, None


while not game_over:
    os.system('clear')
    target_a, target_b = get_targets()
    print_new_round_info(target_a, target_b, player_score)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    round_win, winner = get_round_result(target_a, target_b, choice)
    if round_win:
        last_save_target = winner
        player_score += 1
    else:
        game_over = True
        os.system('clear')
        print(f"Sorry, that's wrong. Final score: {player_score}")