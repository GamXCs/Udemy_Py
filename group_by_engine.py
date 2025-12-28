# records = [
#     {"name": "Alice", "major": "CS", "year": 2},
#     {"name": "Bob", "major": "Math", "year": 1},
#     {"name": "Carol", "major": "CS", "year": 3},
#     {"name": "Dan", "year": 2},  # missing major
#     {"name": "Eve", "major": "Math", "year": 4},
# ]


# def group_by(records, key):
#     # Create empty dictionary to store results
#     groups = {}

#     # We want to look at each record, one at a time
#     for rec in records:
#         label = rec[key]

#     # Check to see if there is already a key created
#         if label not in groups:
#             groups[label] = []
#         groups[label].append(rec["name"])


# items = [
#     ("A", "apple"),
#     ("B", "banana"),
#     ("A", "avocado"),
#     ("B", "blueberry"),
#     ("C", "cherry"),
# ]
# groups = {}

# for letter, fruit in items:
#     if letter not in groups:
#         groups[letter] = []
#     groups[letter].append(fruit)
# print(groups)

# numbers = [1, 2, 3, 4, 5, 6]
# groups = {}

# for num in numbers:
#     if num % 2 == 0:
#         label = "even"
#     else:
#         label = "odd"

#     if label not in groups:
#         groups[label] = []
#     groups[label].append(num)
# print(groups)

# numbers = [3, 15, 8, 22, 1, 30, 12]
# groups = {}

# for num in numbers:
#     if num < 10:
#         label = "small"
#     else:
#         label = "large"

#     if label not in groups:
#         groups[label] = []
#     groups[label].append(num)
# print(groups)

# numbers = [-5, 0, 7, -1, 3, 0, -8]
# new_groups = {}

# for num in numbers:
#     if num < 0:
#         label = "negative"
#     elif num > 0:
#         label = "positive"
#     else:
#         label = "zero"

#     if label not in new_groups:
#         new_groups[label] = []
#     new_groups[label].append(num)
# print(new_groups)


# words = ["cat", "elephant", "dog", "hippopotamus", "ant"]

# groups = {}


# for word in words:
#     if len(word) <= 3:
#         label = "short"
#     else:
#         label = "long"

#     if label not in groups:
#         groups[label] = []
#     groups[label].append(word)
# print(groups)

# grades = [95, 82, 67, 74, 88, 59, 100]
# groups = {}

# for grade in grades:
#     if grade >= 90:
#         label = "A"
#     elif grade >= 80:
#         label = "B"
#     elif grade >= 70:
#         label = "C"
#     else:
#         label = "F"

#     if label not in groups:
#         groups[label] = []
#     groups[label].append(grade)
# print(groups)

# names = ["Alice", "Bob", "Charlie", "Anna", "Brian", "Cathy"]
# groups = {}


records = [
    {"name": "Alice", "major": "CS", "year": 2},
    {"name": "Bob", "major": "Math", "year": 1},
    {"name": "Carol", "major": "CS", "year": 3},
    {"name": "Dan", "year": 2},  # missing major
    {"name": "Eve", "major": "Math", "year": 4},
]


def group_by(records, key, value_key="name", missing="skip"):
    groups = {}

    for rec in records:
        if key not in rec:
            if missing == "skip":
                continue
            elif missing == "group":
                label = "<MISSING>"
            else:
                raise ValueError("missing must be 'skip' or 'group'")
        else:
            label = rec[key]

        # decide what to store
        value = rec.get(value_key)

        # create 'bucket' to store
        if label not in groups:
            groups[label] = []
        groups[label].append(rec.get(value_key))
        # value_key can be anything (name, major, etc)
    print(groups)
