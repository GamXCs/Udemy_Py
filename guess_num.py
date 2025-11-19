import random

# Generate random number
num = random.randint(0, 1000)
print(num)

# Limit number of guesses
guess_attempts = 3

while guess_attempts > 0:
    # Get user number
    user_guess = int(input("Enter a number to guess: "))

    # Conditionals to check if it is correct
    if user_guess == num:
        print("That's correct! You guessed the number!")
        break
    else:
        guess_attempts -= 1
        if guess_attempts > 0:
            print("Sorry, that is not the correct number.\nTry again!")
        else:
            print(f"Sorry, Game Over. The number was {num}")
