# Number Analysis

num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Positive, Negative or Zero
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Leap Year Check
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")