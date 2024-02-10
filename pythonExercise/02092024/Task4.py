# Fibonacci series

print("***Program to print Fibonacci series***")

number = int(input("How many numbers you want to see? "))

i, j, n = 0, 1, 3

if number < 2:
    print("Enter number equal or more than 2!!!!!")
elif number == 2:
    print(i, j)
else:
    print(i, j, end=" ")
    while n <= number:
        a = i + j
        print(a, end=" ")
        i = j
        j = a
        n += 1