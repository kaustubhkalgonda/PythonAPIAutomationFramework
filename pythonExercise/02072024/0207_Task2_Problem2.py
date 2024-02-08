# Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

print("This is a program to compare 2 numbers")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Comparing two numbers, please wait.....")

print(f"First Number is greater than Second Number: {number1 > number2}")
print(f"First Number is equal to Second Number: {number1 == number2}")
print(f"First Number is smaller than Second Number: {number1 < number2}")
