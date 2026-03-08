import string

"""
Frequency Analyzer

Provides tools for analyzing word and character frequencies in text.
"""


def word_frequency(text):

    # Normalize
    text = text.lower()

    # get rid of punctuation w/ string library
    for char in string.punctuation:
        text = text.replace(char, "")

    # turn into a list of words
    words = text.split()

    # create dictionary to store results
    new_dict = {}

    # loop through string and create a count
    for word in words:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict
