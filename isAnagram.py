from collections import Counter

# import collections library using the Counter module

wordOne = input("Enter a word or phrase to check if it's an anagram: ")
wordTwo = input("Enter a word or phrase to check if it's an anagram: ")

wordOne = "".join(letter.lower() for letter in wordOne if letter.isalpha())
wordTwo = "".join(letter.lower() for letter in wordTwo if letter.isalpha())

if Counter(wordOne) == Counter(wordTwo):
    print(f"{wordOne} and {wordTwo} are Anagrams")
else:
    print(f"{wordOne} and {wordTwo} are not Anagrams")
