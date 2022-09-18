import random


def play():

    computer = random.choice(['r', 'p', 's'])

    while True:
        user = input("Please choose 'r' for rock, 'p' for paper, and 's' for scissors\n")
        if (user == 'r') or (user == 'p') or (user == 's'):
            break

    print(f"You chose {user}, and the computer chose {computer}.")

    if user == computer:
        return "It is a tie!"

    # r > s , p > r, s > p
    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    # r > s , p > r, s > p
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") \
        or (player == "s" and opponent == "p"):
        return True

print(play())