print(" FIND THE HEAVIER BALL (2 WEIGHINGS)")
print("\nBalls: A B C D E F G H")

print("\nFirst Weighing:")
print("Compare (A B C) vs (D E F)")

print("\nEnter the result:")
print("1. Left side is heavier\t2. Right side is heavier\t3. Both sides are equal")

choice = int(input("Choice: "))
if choice == 1:
    print("\nSecond Weighing:")
    print("Compare A vs B")

    print("\nEnter the result:")
    print("1. A is heavier\t2. B is heavier\t3. Both are equal")
    choice = int(input("Choice: "))

    if choice == 1:
        print("\nHeavier Ball = A")
    elif choice == 2:
        print("\nHeavier Ball = B")
    else:
        print("\nHeavier Ball = C")

elif choice == 2:

    print("\nSecond Weighing:")
    print("Compare D vs E")

    print("\nEnter the result:")
    print("1. D is heavier\t2. E is heavier\t3. Both are equal")

    choice = int(input("Choice: "))

    if choice == 1:
        print("\nHeavier Ball = D")
    elif choice == 2:
        print("\nHeavier Ball = E")
    else:
        print("\nHeavier Ball = F")

elif choice == 3:

    print("\nSecond Weighing:")
    print("Compare G vs H")

    print("\nEnter the result:")
    print("1. G is heavier\t2. H is heavier")

    choice = int(input("Choice: "))

    if choice == 1:
        print("\nHeavier Ball = G")
    else:
        print("\nHeavier Ball = H")

else:
    print("\nInvalid Choice!")