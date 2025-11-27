import string
from turtle import resetscreen

# Read file
with open(
    "/Users/gamlielibn/Desktop/Personal Projects/text_analyzer_test.txt", "r"
) as f:
    fileContents = f.read()

# Convert text into a clean list of words
char = string.punctuation  # Uses built-in function holding all punctuation
dict = {c: None for c in char}  # Makes a dictionary mapping each char to None
tab = str.maketrans(dict)
result = fileContents.lower().translate(tab).split()

# Build a dictionary with a word count frequency
word_count = 0
count_dict = {}
for word in result:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)
