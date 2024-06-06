employees = [
 ("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith", "Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com") ]

# 1

for name, department, _ in employees:
    print(f"Name: {name}, Department: {department}")

# 2

def get_last_name(employee):
    return employee[0].split()[-1]

sorted_employees = sorted(employees, key=get_last_name)

for _, _, email in sorted_employees:
    print(email)

# 3

new_employee = ("David Wilson", "Sales", "david.wilson@example.com")
employees.append(new_employee)

for employees in employees:
    print(employees)

# 4



