# Create/Open a File
# file = open("students.txt", "w")
# print("File opened successfully.")
# file.close()

# Writing to a Text File
# file = open("students.txt", "w")
# file.write("Anita\n")
# file.write("Rahul\n")
# file.write("Priya\n")
# file.close()
# print("Student details saved successfully.")

# Writing Multiple Lines Using writelines()
# students = ["Anita\n", "Rahul\n", "Priya\n", "Kiran\n"]
file = open("students.txt", "a")
#file.writelines(students)
file.write("Rita\n")
file.close()
