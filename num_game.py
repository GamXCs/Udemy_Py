"""program that takes no arguement
chooses random int between 0 - 100 inclusive
tells "too high","too low", or "just right"
if user guess correctly, program exits
otherwise, try again
"""

"""second iteration do error handling for bad input"""
# numbers entered less than 0
# floats
# words

import random


def guessing_game():

    number = random.randint(0, 100)
    target = number
    print(target)
    num_guess = 3

    while num_guess > 0:
        try:
            user_guess = int(input("Guess a number from 0 - 100: "))

            if user_guess > 100 or user_guess < 0:
                print("Number must be between 0 - 100")
                continue

        except ValueError:
            print(
                "Entry cannot be a decimal or letter. Must be a non-negative integer between 0 - 100."
            )

        num_guess -= 1

        if user_guess == target:
            print(f"Just Right! The answer was {user_guess}")
            break

        elif user_guess < target:
            print("too low")
        else:
            print("too high")


guessing_game()
