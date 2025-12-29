from pprint import pprint

records = [
    {"name": "Alice", "major": "CS", "year": 2, "gpa": 3.8},
    {"name": "Bob", "major": "Math", "year": 1, "gpa": 3.2},
    {"name": "Carol", "major": "CS", "year": 3, "gpa": 3.9},
    {"name": "Dan", "year": 2, "gpa": 2.8},
    {"name": "Eve", "major": "Math", "year": 4, "gpa": 3.6},
]

# Loop through and print records
for rec in records:
    # strip records and title case
    rec["name"] = rec["name"].strip().title()

    # handle missing majors (if major is missing, output 'Undeclared')
    # clean major data
    if "major" not in rec:
        rec["major"] = "Undeclared"
    else:
        rec["major"] = rec["major"].strip().title()

    # normalize year/make sure it is always an int
    rec["year"] = int(rec["year"])

    # make sure gpa is always a float
    rec["gpa"] = float(rec["gpa"])

    # print(rec)

"""Compute: total num of students
    Average gpa
    Min gpa
    Max gpa
    """
# number of students
num_of_students = len(records)
print(f"There are {num_of_students} students")

# Average gpa
gpa = 0
for rec in records:
    gpa += rec["gpa"]
avg_gpa = gpa / num_of_students
print(f"The average gpa is {avg_gpa}")

# Minimum/Maximum gpa
minimum = min(rec["gpa"] for rec in records)
maximum = max(rec["gpa"] for rec in records)
print(f"The minimum gpa is {minimum} and the maximum is {maximum}")

"""Count students and average gpa
    Example Output:
        CS — Count: 2, Avg GPA: 3.85
        Math — Count: 2, Avg GPA: 3.40
        Undeclared — Count: 1, Avg GPA: 2.80
        """
# group by major use label
groups = {}

for rec in records:
    major = rec["major"]

    if major not in groups:
        groups[major] = []
    groups[major].append(rec)

for major, students in groups.items():
    count = len(students)
    average_gpa = sum(s["gpa"] for s in students) / count
    print(f"{major} - Count: {count}, Avg gpa: {average_gpa:.2f}")
