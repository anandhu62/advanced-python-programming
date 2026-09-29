from university.student import student_details
from university.result import calculate_percentage

student_details("Anita", "MCA")
marks = [85, 90, 78, 88]
percentage = calculate_percentage(marks)
print("Percentage:", percentage)