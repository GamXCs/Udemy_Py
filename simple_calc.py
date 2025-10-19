# Design a simple calculator
def main():
    while True:
        if input("Do you want to calculate again? (y/n) ").lower() == "n":
            break
        a = get_number("Enter a first number: ")
        b = get_number("Enter a second number: ")
        sign = input("Enter a sign: (+-*/)\nType q to quit ")

        # Provide option to quit the calculator
        if sign == "q":
            print("Goodbye")
            break

        if sign in choose_sign:
            name, operation = choose_sign[sign]
            result = operation(a, b)
            print(f"The result of {name} is: {result}")
        else:
            print("Invalid operation. Please enter one of +,-,*,/")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return a / b


choose_sign = {
    "+": ("Addition", add),
    "-": ("Subtraction", subtract),
    "*": ("Multiplication", multiply),
    "/": ("Divide", divide),
}


# Prompt user for a number by passing a prompt
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: please enter a valid number: ")


if __name__ == "__main__":
    main()
