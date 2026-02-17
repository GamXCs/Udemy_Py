def parse_int(test_str):
    test_str = test_str.strip()  # get rid of whitespace

    # check if input is empty
    if len(test_str) == 0:
        raise ValueError("String cannot be empty")

    # use sign as a multiplier to read input and assgn the
    # correct value
    sign = 1
    if test_str[0] in ["+", "-"]:
        if test_str[0] == "-":
            sign = -1
    test_str = test_str[1:]

    # handle if input is only a sign with no numbers
    if len(test_str) == 0:
        raise ValueError("Sign must be followed by digits")

    # check if there are any non-numbers is input
    for letter in test_str:
        if not letter.isdigit():
            raise ValueError("String must be a number")

    return sign * int(test_str)


def parse_float(test_str):
    test_str = test_str.strip()  # get rid of whitespace

    # check if input is empty
    if len(test_str) == 0:
        raise ValueError("String cannot be empty")

    # use sign as a multiplier to read input and assgn the
    # correct value
    sign = 1
    if test_str[0] in ["+", "-"]:
        if test_str[0] == "-":
            sign = -1
    test_str = test_str[1:]

    # handle if input is only a sign with no numbers
    if len(test_str) == 0:
        raise ValueError("Sign must be followed by digits")

    # check for "." in string
    dots = 0
    digit_count = 0
    for letter in test_str:
        digit_count += 1
        if letter == ".":
            dots += 1
    if dots == 1 and digit_count >= 1:
        return sign * float(test_str)


print(parse_int("   -123  \n"))
print(parse_float("   -123.33  "))
