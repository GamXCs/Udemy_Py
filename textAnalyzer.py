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

count_dict = {}
for word in result:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

# Count total number of words
wordCount = len(result)
print(f"The total number of words: {wordCount}\n")

# Count total number of unique words (Number of keys)
uniqueWords = len(count_dict)
print(f"Total number of unique words: {uniqueWords}\n")

# Count most common word
print(max(count_dict, key=lambda mostCommon: count_dict[mostCommon]))
