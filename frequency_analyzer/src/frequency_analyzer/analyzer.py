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
        text = text.split(start_marker, 1)[1]  # cut off the slice
    if end_marker in text:
        text = text.split(end_marker, 1)[0]

    return text


# lowercase the text and remove punctuation
def clean_text(text):
    text = text.lower()

    for char in string.punctuation:
        teext = text.replace(char, "")
    return text


# split on whitespace and return a list of words
def tokenize(text):
    return text.split()


# count words
def count_words(words):
    return Counter(words)


def word_frequency(text):
    text = clean_text(text)
    words = tokenize(text)
    return count_words(words)


# return n most common words
def top_n_words(word_counts, n=10):
    return word_counts.most_common(n)


# ignore spaces, punctuation, eventually plot frequencies w/ matplotlib
def char_frequency(text):
    pass
