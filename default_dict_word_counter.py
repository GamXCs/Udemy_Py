import csv
from collections import defaultdict

# initialize defautdict
word_count = defaultdict(int)

with open("csv_practice.csv", mode="r") as file:
    csv_words = csv.reader(file)
    next(csv_words)

    for lines in csv_words:
        words = lines[2].lower().split()

        for word in words:
            clean_word = word.strip("!,.?:;")

            word_count[clean_word] += 1

for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
    print(f"{word}: {count}")
