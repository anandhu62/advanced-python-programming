# Pattern 1

print("Pattern 1")
for i in range(1, 6):
    print("*" * i)

# Pattern 2

print("\nPattern 2")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern 3

print("\nPattern 3")
for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()

# Pattern 4

print("Pattern 4")

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))