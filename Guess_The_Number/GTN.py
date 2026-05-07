# https://github.com/YaogoGerard
"""
This a program that propose to the user to try to find an mysterious number
"""

import random


def guess_the_number(n):
    mysterious_number = random.randint(1, n)
    user_number = int(input("Enter your guess: "))
    counter: int = 1  # this counter give the number of attempts
    while user_number != mysterious_number:
        if user_number > mysterious_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        user_number = int(input("Enter your guess: "))
        counter += 1
    print(
        f"Congratulations you are find the mysterious number {mysterious_number} in {counter} attempts!"
    )


guess_the_number(10)
