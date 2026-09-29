# Loop-Based Problems

n = int(input("Enter a positive integer: "))

print("\nNumbers from 1 to", n)
for i in range(1, n + 1):
    print(i, end=" ")

print("\n\nMultiplication Table")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("\nFactorial =", factorial)

print("\nFibonacci Series")

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b