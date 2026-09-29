# Prime Number Operations

num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not Prime")

start = int(input("\nEnter Start Range: "))
end = int(input("Enter End Range: "))

print("\nPrime Numbers:")

for number in range(start, end + 1):

    if number > 1:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number, end=" ")