#Anagrams Strings

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if string1 == string2:
    print("These strings are not Anagrams")
else:
    string1List = []
    string2List = []

    for letter1 in string1:
        string1List.append(letter1.lower())
    for letter2 in string2:
        string2List.append(letter2.lower())

    string1List.sort()
    string2List.sort()

    if string1List == string2List:
        print("These strings are Anagrams")
    else:
        print("These strings are not Anagrams")