from hmac import digest_size


def int_parser(string):

    # validate the string
    # strip whitespace, detect optional sign, ensure characters are digits
    # convert to int, apply sign

    s = string.strip()

    # check if string is empty
    if not s:
        raise ValueError("String is empty")

    # check for sign and remove it
    sign = 1
    if s[0] in "-+":
        if s[0] == "-":
            sign = -1
        s = s[1:]

    # if not s is more pythonic than if len(s) == 0
    if not s:
        raise ValueError("String is empty")

    for char in s:
        if not char.isdigit():
            raise ValueError("String must only containbe numbers")

    return sign * int(s)


# -----------Test Cases--------------
print(int_parser("     -123    "))
print(int_parser("     23    "))
print(int_parser("     +3123    "))


def float_parser(string):
    # validate the string
    # strip whitespace, detect optional sign, ensure characters are digits
    # convert to int, apply sign

    s = string.strip()

    # check if string is empty
    if not s:
        raise ValueError("String is empty")

    # check for sign and remove it
    sign = 1
    if s[0] in "-+":
        if s[0] == "-":
            sign = -1
        s = s[1:]

    # if not s is more pythonic than if len(s) == 0
    if not s:
        raise ValueError("String is empty")

    dot_count = 0
    digit_count = 0

    for char in s:
        if char.isdigit():
            digit_count += 1
        elif char == ".":
            dot_count += 1
            if dot_count > 1:
                raise ValueError("String can only contain one decimal")
        else:
            raise ValueError("Invalid input")

    if digit_count == 0:
        raise ValueError("Float must contain at least one digit")

    return sign * float(s)


print(float_parser("3.14"))
print(float_parser(".5"))
print(float_parser("5."))
print(float_parser("   -0.25  "))
print(float_parser("+12.0"))
