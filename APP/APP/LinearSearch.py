# char-by-char reading
word = "Python"

for ch in word:
    print(ch)

# Linear Search using for...else

numbers = [12, 45, 67, 23, 89, 34, 56]

key = int(input("Enter the number to search: "))

for item in numbers:
    if item == key:
        print(f"{key} found.")
        break
else:
    print(f"{key} not found.")

# enumerate() function
colors = ["Red", "Green", "Blue"]

for index, color in enumerate(colors):
    print(index, color)

# zip() function
names = ["A", "B", "C"]
marks = [80, 90, 85]

for name, mark in zip(names, marks):
    print(name, mark)

# Reversed order using reversed() function
for i in reversed(range(5)):
    print(i)

#reverse using while loop
count = 5
while count > 0:
    print(count)
    count -= 1

# Dictionary Iteration 
student = {"Name":"Sam", "Age":20}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-Value pairs
for key, value in student.items():
    print(key, value)

# Iterating over a list of tuples
students = [("Alice", 85), ("Bob", 90), ("Charlie", 88)]

for name, marks in students:
    print(name, marks)

# Sorting the list in ascending order
numbers = [5, 2, 8, 1]
for num in sorted(numbers):
    print(num)