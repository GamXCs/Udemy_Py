# Reverse a string

S1 = input("Enter a word to reverse it: ")
S2 = S1.strip()

rev_word = S2[::-1]

if S1.casefold() == rev_word.casefold():
    print(rev_word)
else:
    palindrome = S1.casefold() + rev_word.casefold()
    print(palindrome)
