# 1.

students = {"Alice": [85, 78, 92],
 "Bob": [79, 74, 81],
 "Charlie": [91, 82, 85],
 "David": [76, 85, 83],
 "Eve": [88, 79, 92]}

avgstudents = {}
for k,v in students.items():
    avgstudents[k] = sum(v) / float(len(v))

print(avgstudents)

# 2.

top_student = max(avgstudents)
print(f"The student with the highest average is {top_student}")

# 3.

lowavgstu = min(avgstudents)
print(f"The student with the lowest average is {lowavgstu}")


# 4.

students["Frank"] = [80, 90, 85]
print(students)