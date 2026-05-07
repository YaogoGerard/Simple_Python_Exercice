# https://github.com/YaogoGerard
"""
This a simple program to game the game  of Rock, Paper and Scissors.
"""

import random

user_choice = input(
    "Enter (R) for the Rock, (P) for the Paper and (S) for the Scissors: "
)
computer_choice = random.choice(["R", "P", "S"])


def play(u_c, c_c):
    if u_c == c_c:
        print("Try again")
        uc = input(
            "Enter (R) for the Rock, (P) for the Paper and (S) for the Scissors: "
        )
        cc = random.choice(["R", "P", "S"])
        play(uc, cc)
    # I suppose all possiblitities
    elif (
        (u_c == "R" and c_c == "S")
        or (u_c == "P" and c_c == "R")
        or (u_c == "S" and c_c == "P")
    ):
        print("You win!")
    else:
        print("Computer wins!")


play(user_choice, computer_choice)
