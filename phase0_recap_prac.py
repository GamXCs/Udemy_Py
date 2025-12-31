from pprint import pprint

employees = [
    {"name": " alice ", "department": "Engineering", "salary": "85000"},
    {"name": "Bob", "department": "Sales", "salary": 72000},
    {"name": "Carol", "department": "Engineering", "salary": "91000"},
    {"name": "Dan", "salary": 60000},
    {"name": "Eve", "department": "Sales", "salary": "78000"},
]

# Clean the data (title/case)
for employee in employees:
    employee["name"] = employee["name"].strip().title()
    employee["salary"] = int(employee["salary"])

    if "department" not in employee:
        employee["department"] = "Unassigned"
    else:
        employee["department"] = employee["department"].strip().title()
# pprint(employees)

"""Total number of employees
    Average salary
    Min salary
    Max salary
    """

# Number of employees and average salary
num_employees = len(employees)
salary = 0
for employee in employees:
    salary += employee["salary"]
avg_salary = salary / num_employees
print(f"There are {num_employees} employees.\nThe average salary is ${avg_salary:.2f}")

# Minimum and maximum salary
minumum = min(employee["salary"] for employee in employees)
maximum = max(employee["salary"] for employee in employees)
print(f"The lowest salary is ${minumum:.2f} and the highest is ${maximum:.2f}")

"""Group stats by department
    For each department, count employees and give the avg salary"""
groups = {}

for employee in employees:
    department = employee["department"]

    if department not in groups:
        groups[department] = []
    groups[department].append(employee)

for department, employees_in_dept in groups.items():
    count = len(employees_in_dept)
    average_salary = sum(e["salary"] for e in employees_in_dept) / count
    print(f"Department: {department} - {count}, Average Salary: ${average_salary:.2f}")
