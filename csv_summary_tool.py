# import csv

# """ Create function to open file, read lines, strip whitespace,
# ignore blank lines, convert to float, handle type and/or value errors
# return list of floats"""


def load_numbers(filename):
    # list to store numbers from csv
    numbers_from_csv = []

    # open file
    with open(filename, mode="r") as file:
        for line in file:
            cleaned = line.strip()

            # check for empty line
            if cleaned == "":
                continue

            try:
                line = float(cleaned)
            except ValueError:
                raise TypeError("Invalid value")

            numbers_from_csv.append(line)

    return numbers_from_csv


def main():
    # Step 1: load data or define inputs
    pass

    # Step 2: process
    pass

    # Step 3: output results
    pass

    filename = "data.csv"
    print(load_numbers(filename))


if __name__ == "__main__":
    main()
