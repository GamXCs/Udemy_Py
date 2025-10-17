# Given a string containing mixed characters, construct a new string that includes
# only alphabetic characters and spaces. Replace every other character with a space.

from xxlimited import new


scan = "These+notes#reveal9Newton seeking-out an{underlying structure to/the\pyramid}"

clean = ""

# TODO:Write the  Data Cleaning Logic using for loop below
for char in scan:
    if char.isalpha() or char.isspace():
        clean += char
    else:
        clean += " "


print(clean)
