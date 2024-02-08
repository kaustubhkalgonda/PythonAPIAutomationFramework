# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2
# ( Take pie as 3.14)

print("This is a program to calculate the area of a circle.")
radius = float(input("Please enter Radius of the circle: "))
pi = 3.14
print("Calculating Area of the circle........")
print()

area = pi * (radius ** 2)

print(f"Area of the circle is: {area}")
