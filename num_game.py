"""program that takes no arguement
chooses random int between 0 - 100 inclusive
tells "too high","too low", or "just right"
if user guess correctly, program exits
otherwise, try again
"""

import random


def guessing_game():

    number = random.randint(0, 100)
    target = number
    print(target)

    while True:
        user_guess = int(input("Guess a number from 0 - 100: "))

        if user_guess == target:
            print(f"Just Right! The answer was {user_guess}")
            break

        elif user_guess < target:
            print("too low")
        else:
            print("too high")


guessing_game()
