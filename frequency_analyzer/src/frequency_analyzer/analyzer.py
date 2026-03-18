import string
from collections import Counter

"""
Frequency Analyzer

Provides tools for analyzing word and character frequencies in text.
"""


# function to remove the header from gutenburg website
def remove_gutenberg_header(text):

    # look for the gutenberg header and end
    start_marker = "*** START OF"
    end_marker = "*** END OF"

    # use split to cut off the header and footer
    if start_marker in text:
        text = text.split(start_marker, 1)[1]
    if end_marker in text:
        text = text.split(end_marker, 1)[0]

    return text


def word_frequency(text):

    # Normalize
    text = text.lower()

    # get rid of punctuation w/ string library
    for char in string.punctuation:
        text = text.replace(char, "")

    # turn into a list of words
    words = text.split()

    return Counter(words)
