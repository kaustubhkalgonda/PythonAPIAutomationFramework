# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
#
# Example - pramod
# madam - reverse(madam) -> same
# Naman -> reverse -> same
# Malayalam

def str_checker(inputString):
    strLength = len(inputString)
    isPalindrome = True

    for i in range(int(strLength / 2)):
        if inputString[i] == inputString[strLength - 1 - i]:
            isPalindrome = True
        else:
            isPalindrome = False
            break
    return isPalindrome


userString = input("Enter string to be verified: ").lower()
print(f"{userString} is Palindrome: {str_checker(userString)}")
