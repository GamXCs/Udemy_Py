# """ Create function to open file, read lines, strip whitespace,
# ignore blank lines, convert to float, handle type and/or value errors
# return list of floats"""
from summary_lib import summarize


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
                value = float(cleaned)
            except ValueError:
                raise TypeError("Invalid value")

            numbers_from_csv.append(value)

    return numbers_from_csv


def main():
    try:
        nums = load_numbers("data.csv")
        summary = summarize(nums)

        print("Summary Report")
        print("-" * 20)
        for key, value in summary.items():
            print(f"{key}:{value}")
    except Exception as e:
        print(f"Error: {e}")
    # filename = "data.csv"
    # print(load_numbers(filename))


if __name__ == "__main__":
    main()
