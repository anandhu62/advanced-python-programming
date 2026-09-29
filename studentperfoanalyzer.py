import random
from datetime import date
from collections import Counter
from functools import reduce

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

#average and total marks
averages = {}

for name, marks in students.items():
    total = reduce(lambda x, y: x + y, marks)
    average = total / len(marks)

    averages[name] = average

    print(name)
    print("Total Marks:", total)
    print("Average:", average)
    print()

#student with highest average
highest_student = max(averages, key=averages.get)

print("Highest Average:")
print(highest_student, ":", averages[highest_student])

#Random selection
selected_student = random.choice(list(students.keys()))

print("\nRandomly Selected Student:")
print(selected_student)

#current date
print("\nCurrent Date:")
print(date.today())

#grades

grades = []

for average in averages.values():
    if average >= 90:
        grades.append("A")
    elif average >= 80:
        grades.append("B")
    elif average >= 70:
        grades.append("C")
    else:
        grades.append("D")

grade_count = Counter(grades)

print("\nGrade Classification:")
print(grade_count)