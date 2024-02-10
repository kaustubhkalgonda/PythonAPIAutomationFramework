# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

print("***Program to classify triangle***")
side1 = int(input("Please enter side1 length: "))
side2 = int(input("Please enter side2 length: "))
side3 = int(input("Please enter side3 length: "))

if side1 == side2 and side1 == side3:
    print("This is Equilateral Triangle.")
elif side1 != side2 and side1 != side3 and side2 != side3:
    print("This is Scalane Triangle.")
elif (side1 == side2 and side1 != side3 and side2 != side3) or (
        side1 != side2 and side1 == side3 and side2 != side3) or (
        side1 != side2 and side1 != side3 and side2 == side3):
    print("This is Isoceles Triangle.")
