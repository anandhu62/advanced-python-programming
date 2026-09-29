# Student Information System

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
course = input("Enter Course: ")
semester = input("Enter Semester: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter Marks in Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B+"
elif percentage >= 50:
    grade = "B"
else:
    grade = "F"

print("\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll)
print("Course:", course)
print("Semester:", semester)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)