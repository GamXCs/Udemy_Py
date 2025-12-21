from pprint import pprint

gradebook = {
    "Ava": [88, 92, 79],
    "Ben": [100, 73],
    "Cam": [90, 90, 91],
    "Dee": [],
    "Eli": [65, 70, 72],
}


# Function to calculate letter grade
def grade_calc(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Add new grade
name = "Gam"
new_grade = 98
summary = {}

gradebook.setdefault(name, []).append(new_grade)
print(gradebook)

# Compute average per student
for name, grades in gradebook.items():
    # If there are no grades in the list, skip to next
    if len(grades) == 0:
        continue

    # Compute values to store in summary dictionary
    average = sum(grades) / len(grades)
    letter = grade_calc(average)
    minimum = min(grades)
    maximum = max(grades)
    count = len(grades)

    summary[name] = {
        "avg": average,
        "grade": letter,
        "lowest grade": minimum,
        "highest grade": maximum,
        "count": count,
    }

pprint(summary)

# Build a summary dictionary
