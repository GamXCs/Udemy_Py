from number_parser.parser import parse_float, parse_int

print(parse_int("   -123   "))
print(parse_float("3.14"))
print(parse_float(".5"))
print(parse_float("5."))
print(parse_float("   -0.25   "))
