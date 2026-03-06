# TODO: #implement parse_number(): make function that decides what type and choose


class ParseNumberError(ValueError):
    """Raised when a string cannot be parsed as a number."""

    pass


# renamed the functions to follow common API convention:
# action_object


def parse_int(string):

    # validate the string
    # strip whitespace, detect optional sign, ensure characters are digits
    # convert to int, apply sign

    s = string.strip()

    # check if string is empty
    if not s:
        raise ParseNumberError("Input string is empty")

    # check for sign and remove it
    sign = 1
    if s[0] in "-+":
        if s[0] == "-":
            sign = -1
        s = s[1:]

    # if not s is more pythonic than if len(s) == 0
    if not s:
        raise ParseNumberError("Input string is empty")

    for char in s:
        if not char.isdigit():
            raise ParseNumberError("String must only contain numbers")

    return sign * int(s)


def parse_float(string):
    # validate the string
    # strip whitespace, detect optional sign, ensure characters are digits
    # convert to int, apply sign

    s = string.strip()

    # check if string is empty
    if not s:
        raise ParseNumberError("String is empty")

    # check for sign and remove it
    sign = 1
    if s[0] in "-+":
        if s[0] == "-":
            sign = -1
        s = s[1:]

    # if not s is more pythonic than if len(s) == 0
    if not s:
        raise ParseNumberError("String is empty")

    dot_count = 0
    digit_count = 0

    for char in s:
        if char.isdigit():
            digit_count += 1
        elif char == ".":
            dot_count += 1
            if dot_count > 1:
                raise ParseNumberError("Multiple decimal points found")
        else:
            raise ParseNumberError("Invalid input")

    if digit_count == 0:
        raise ParseNumberError("Float must contain at least one digit")

    return sign * float(s)
