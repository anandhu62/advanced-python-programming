# different methods to inspect file properties:
# file = open("students.txt", "r+")

# readcontent = file.read()
# file.write("\nThank you.")

# print("Read Content:\n", readcontent)
# print("File Name:", file.name)
# print("File Mode:", file.mode)
# print("File Closed:", file.closed)

# The with statement automatically closes the file.
# with open("students.txt", "a") as file:
#     name = input("Enter new student name: ")
#     file.write(name + "\n")
# print("Student added successfully.")
# print("File Closed:", file.closed)

# Counting Lines, Words, and Characters in a File
# with open("students.txt", "r") as file:
#     content = file.read()
# lines = content.splitlines() # The splitlines() method splits the content into a list of lines, removing the newline characters.
# words = content.split() # The split() method splits the content into a list of words, using whitespace as the delimiter.
# characters = len(content) # The len() function returns the number of characters in the content, including whitespace and newline characters.
# print("Number of Lines:", len(lines))
# print("Number of Words:", len(words))
# print("Number of Characters:", characters)

# The file pointer tell()indicates the current position in the file.
# with open("students.txt", "r") as file:
#     print("Initial position:", file.tell())
#     print(file.read(5))
#     print("Position after reading:", file.tell())

#seek() moves the file pointer to a specific position.
with open("students.txt", "r") as file:
    print("Initial text:", file.read(10))
    print("Position before seeking:", file.tell())
    file.seek(5)
    print("Position after seeking:", file.tell())
    print("Current text:", file.read(6))