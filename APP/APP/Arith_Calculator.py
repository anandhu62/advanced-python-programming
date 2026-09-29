# Arithmetic Calculator
#input two numbers from user and perform arithmetic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# formatting the output to display the results of arithmetic operations
print("\nArithmetic Operations")
print(f"Addition of {num1} and {num2} = {num1 + num2}")
print(f"Subtraction of {num1} and {num2} = {num1 - num2}")
print(f"Multiplication of {num1} and {num2} = {num1 * num2}")
print(f"Division of {num1} and {num2} = {num1 / num2}")
print(f"Floor Division of {num1} and {num2} = {num1 // num2}")
print(f"Modulus of {num1} and {num2} = {num1 % num2}")
print(f"Exponentiation of {num1} and {num2} = {num1 ** num2}")