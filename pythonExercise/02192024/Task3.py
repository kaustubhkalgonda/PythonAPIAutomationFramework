#Find a substring in a String.

string1 = input("Enter a string: ")
substring = input("Enter sub string to be searched: ")

if substring in string1:
    print(f"{substring} is present in: {string1}")
else:
    print(f"{substring} is not present in: {string1}")

if string1.find(substring) != -1:
    print(f"{substring} is present in: {string1}")
else:
    print(f"{substring} is not present in: {string1}")
