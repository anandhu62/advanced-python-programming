# Menu-Driven Calculator

while True:

    print("\n========== Calculator ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    if choice >= 1 and choice <= 4:

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:

            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero is not allowed.")

    else:
        print("Invalid Choice")