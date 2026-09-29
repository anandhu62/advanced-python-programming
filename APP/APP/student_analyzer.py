# to utilize a student utility module
import student_utils

marks = [85, 91, 78, 88, 82]

total = student_utils.calculate_total(marks)
percentage = student_utils.calculate_percentage(marks)
grade = student_utils.find_grade(percentage)

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)