# Print the Table of 2 by using the command print()

num = int(input("Enter Number to print Table: "))
limit = int(input("Enter Number for table limit: "))

print("Here is your table for {0} :".format(num))

i = 1

while i <= limit:
    print("{0} x {1} = {2}".format(num, i, num*i))
    i += 1
