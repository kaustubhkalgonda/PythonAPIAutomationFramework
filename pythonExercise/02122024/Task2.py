# Implement a Function to Calculate the Factorial of a Number

def factorial_checker(number):
    if number == 0:
        print("Factorial for 0 is 1.")
    else:
        result = 1
        for i in range(1, number + 1):
            result = result * i
        print(f"Factorial for {number} is: {result}")


number = int(input("Enter a number: "))
factorial_checker(number)
