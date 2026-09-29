# Reading a Complete File
# file = open("students.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Reading a Specific Number of Characters
# file = open("students.txt", "r")
# content = file.read(10)  # The read(n) method reads n characters.
# print(content)
# file.close()

# Reading One Line at a Time
file = open("students.txt", "r")
line = file.readline()
print("Read Line Content:\n", line)
file.close()

# Reading All Lines into a List
# file = open("students.txt", "r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# Reading All Lines Using readlines()
# file = open("students.txt", "r")
# lines = file.readlines()  # Notice that readlines() returns a
#                             # list of strings.
# print(lines)
# file.close()

# Reading a File Using a for Loop
file = open("students.txt", "r")
for line in file:
    print(line.strip())  # The strip() method removes any leading and trailing whitespace characters, including the newline character at the end of each line.
file.close()
