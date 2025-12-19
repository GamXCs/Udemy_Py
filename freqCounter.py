"""Frequency counter: input is a list of strings or numbers
output: dictionary{item:count)
case-insensitive for strings
ignore empty values
sort results by frequency
return top-k items
"""

print("RUNNING NEW VERSION")
data = [
    "Apple",
    "banana",
    "APPLE",
    "orange",
    "Banana",
    "apple",
    "",
    "Orange",
    None,
    "banana",
    "pear",
    "PEAR",
    "pear",
    "kiwi",
    "Kiwi",
    "KIWI",
    "apple ",
    " banana",
    "grape",
    "Grape",
    "grape",
    42,
    42,
    7,
    7,
    7,
    "42",
    "7",
    "",
]

# Create dictionary

counts = {}

for entry in data:
    if entry is None:
        continue

    # Check if each word is a string
    if isinstance(entry, str):
        entry = entry.lower().strip()

        if entry == "":
            continue

    counts[entry] = counts.get(entry, 0) + 1
print(counts)
