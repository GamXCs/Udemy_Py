import csv

with open("csv_practice.csv", mode="r") as f:
    csv_file = csv.reader(f)

    # skip header row
    header = next(csv_file)

    # empty dictionary
    word_count = {}

    for lines in csv_file:
        # get only the text [id, category, content]
        content = lines[2]
        print(content)

        words = content.split()

        for word in words:
            # clean words
            cleaned_word = word.lower().strip(",.?!")

            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
        print(word_count)
