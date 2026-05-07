# https://github.com/YaogoGerard
"""
This program allow user to try to find a mysterious word by guessing the letter one by one .
"""

import random
import string

from word_list import words

word = random.choice(words).upper()


def challenge(n: int = 7):
    # all of them is a list
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = n

    while len(word_letters) > 0 and lives > 0:
        print(
            f"player live={lives} and you are used these letters: {' '.join(used_letters)}"
        )
        # it is an condition to display the word step by step , if you find a new letter in the word
        display_word = [letter if letter in used_letters else "_" for letter in word]
        print(f"Current word: {' '.join(display_word)}")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"Sorry, you lost! The word was {word}.")
    else:
        print(f"Congratulations, you guessed the word {word}!")


challenge(10)
