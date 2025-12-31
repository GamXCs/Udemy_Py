# from pprint import pprint

# records = [
#     {"name": "Alice", "major": "CS", "year": 2, "gpa": 3.8},
#     {"name": "Bob", "major": "Math", "year": 1, "gpa": 3.2},
#     {"name": "Carol", "major": "CS", "year": 3, "gpa": 3.9},
#     {"name": "Dan", "year": 2, "gpa": 2.8},
#     {"name": "Eve", "major": "Math", "year": 4, "gpa": 3.6},
# ]

# # Loop through and print records
# for rec in records:
#     # strip records and title case
#     rec["name"] = rec["name"].strip().title()

#     # handle missing majors (if major is missing, output 'Undeclared')
#     # clean major data
#     if "major" not in rec:
#         rec["major"] = "Undeclared"
#     else:
#         rec["major"] = rec["major"].strip().title()

#     # normalize year/make sure it is always an int
#     rec["year"] = int(rec["year"])

#     # make sure gpa is always a float
#     rec["gpa"] = float(rec["gpa"])

#     # print(rec)

# """Compute: total num of students
#     Average gpa
#     Min gpa
#     Max gpa
#     """
# # number of students
# num_of_students = len(records)
# print(f"There are {num_of_students} students")

# # Average gpa
# gpa = 0
# for rec in records:
#     gpa += rec["gpa"]
# avg_gpa = gpa / num_of_students
# print(f"The average gpa is {avg_gpa}")

# # Minimum/Maximum gpa
# minimum = min(rec["gpa"] for rec in records)
# maximum = max(rec["gpa"] for rec in records)
# print(f"The minimum gpa is {minimum} and the maximum is {maximum}")

# """Count students and average gpa
#     Example Output:
#         CS — Count: 2, Avg GPA: 3.85
#         Math — Count: 2, Avg GPA: 3.40
#         Undeclared — Count: 1, Avg GPA: 2.80
#         """
# # group by major use label
# groups = {}

# for rec in records:
#     major = rec["major"]

#     if major not in groups:
#         groups[major] = []
#     groups[major].append(rec)

# for major, students in groups.items():
#     count = len(students)
#     average_gpa = sum(s["gpa"] for s in students) / count
#     print(f"{major} - Count: {count}, Avg gpa: {average_gpa:.2f}")


from pprint import pprint

# courses = [
#     {"student": " alice ", "course": "Math", "grade": "88"},
#     {"student": "Bob", "course": "CS", "grade": 92},
#     {"student": "Carol", "course": "Math", "grade": "79"},
#     {"student": "Dan", "course": "CS", "grade": 85},
#     {"student": "Eve", "course": "History", "grade": "90"},
# ]

# for course in courses:
#     course["student"] = course["student"].strip().title()
#     course["course"] = course["course"].strip().title()
#     course["grade"] = int(course["grade"])

# # Summary stats: min/max grades
# num_courses = len(courses)
# minimum = min(course["grade"] for course in courses)
# maximum = max(course["grade"] for course in courses)

# # Average grade overall
# avg = 0
# for course in courses:
#     avg += course["grade"]
# avg_grade = avg / num_courses
# print(f"Average grade: {avg_grade}")

# # Group by course
# groups = {}

# for course in courses:
#     course_name = course["course"]

#     if course_name not in groups:
#         groups[course_name] = []
#     groups[course_name].append(course)

# # Count students and average grade
# for course_name, students in groups.items():
#     count = len(students)
#     a_grade = sum(g["grade"] for s in students) / count
#     print(f"{course_name}:Count- {count}, Average Grade: {a_grade} ")

sales = [
    {"product": " apple ", "category": "Fruit", "price": "0.50"},
    {"product": "Banana", "category": "Fruit", "price": 0.30},
    {"product": "Milk", "category": "Dairy", "price": "2.50"},
    {"product": "Cheese", "category": "Dairy", "price": 4.00},
    {"product": "Bread", "price": "3.00"},
]

# Clean data and account for missing (make Other)
for sale in sales:
    sale["product"] = sale["product"].strip().title()
    sale["price"] = float(sale["price"])
    if "category" not in sale:
        sale["category"] = "Other"
    else:
        sale["category"] = sale["category"].strip().title()

# Avg/min/max price
minimum = min(sale["price"] for sale in sales)
maximum = max(sale["price"] for sale in sales)

total = 0
num_items = len(sales)
for sale in sales:
    total += sale["price"]
avg = total / num_items
# print(f"Average price: ${avg}")

# Group by category
groups = {}

for sale in sales:
    category = sale["category"]

    if category not in groups:
        groups[category] = []
    groups[category].append(sale)

# Count Products/Avg Price
for category_item, products in groups.items():
    count = len(products)
    avg_price = sum(p["price"] for p in products) / count
    print(f"{category_item}:Count- {count}, Average Price: {avg_price}")
