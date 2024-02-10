# Factorial Program

print("***Program to print Factorial of a number***")

number = int(input("Enter a number: "))

if number == 0:
    print("Factorial for 0 is 1.")
else:
    result = 1
    for i in range(1, number + 1):
        result = result * i
    print(f"Factorial for {number} is: {result}")