gradebook = {
    "Ava": [88, 92, 79],
    "Ben": [100, 73],
    "Cam": [90, 90, 91],
    "Dee": [],
    "Eli": [65, 70, 72],
}

# Add new grade
name = "Gam"
new_grade = 98

gradebook.setdefault(name, []).append(new_grade)
print(gradebook)

# Compute average per student
for name, grades in gradebook.items():
    # If there are no grades in the list, skip to next
    if len(grades) == 0:
        continue
    # Compute average
    average = sum(grades) / len(grades)
    print(name, average)

# def gradeCalc(grade):
