#Count vowels and consonants in a String.

userInput = input("Enter a sentence: ")

vowels = ['a','e','i','o','u']

vowelsCount = 0
spacesCount = 0
consonantsCount = 0

for letter in userInput:
    if letter.lower() in vowels:
        vowelsCount+=1
    elif letter.lower()==" ":
        spacesCount +=1
    else:
        consonantsCount+=1

print(f"Vowels: {vowelsCount}\nSpaces: {spacesCount}\nConsonants: {consonantsCount}")