#simple if
#age = int(input("Enter your age: "))
#if age >= 18:
#print("You are eligible to vote.")

#if else
#marks = int(input("Enter your marks: "))
#if marks >=40:
 #print("You have passed the exam.")
#else:
 #print("You have failed the exam.")

#amount=int(input("Enter the amount: "))
#if amount >= 10000:
 #   discount = amount * 0.10
#else:
 #   discount = amount * 0.05
#final_amount = amount - discount
#print("Final amount after discount:", final_amount)

#sal1=int(input("Enter the salary of employee 1: "))
#sal2=int(input("Enter the salary of employee 2: "))

#if sal1 > sal2:
 #   print("Employee 1 has a higher salary.")
#else:
 #   print("Employee 2 has a higher salary.")

#age =int(input("Enter your age: "))
#is_student=False
#discount=True

#if age < 18 and is_student or discount:
#print("You are eligible for a student discount.")

#year=int(input("Enter the year: "))
#print(year, "is a leap year.") if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else print(year, "is not a leap year.")
   
#marks = int(input("Enter your marks: "))
#print("O") if marks >=90 else\
#print("A") if marks >=80 else\
#print("B") if marks >=70 else\
#print("C") if marks >=60 else\
#print("D") if marks >=50 else\
#print("F")

#temp=int(input("Enter the temperature in Celsius: "))
#day=input("Enter the day of the week: ")

#if temp>20 and day.lower() in ["saturday", "sunday"]:
 #   print("It's a warm weekend!")
#else:
 #   print("It's not a warm weekend.")

#n=int(input("Enter a number:"))
#i=1
#a=0
#b=1
#fibonacci_series=[]

#while i <= n:
 #   fibonacci_series.append(a)
  #  a, b = b, a + b
   # i += 1

#print("Fibonacci series:\n")
#print(*fibonacci_series)


for i in reversed(range(5)):
    print(i)