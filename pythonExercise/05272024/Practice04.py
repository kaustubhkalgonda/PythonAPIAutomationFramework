# Character frequency Count from a give String

test_word = "Kaustubh Kalgonda"

result_dict = {}

for char in test_word:
    count = 1
    if char in result_dict.keys():
        count = 1 + result_dict.get(char)
    result_dict[char] = count

for key in result_dict:
    print(f"Character {key} is repeated {result_dict.get(key)} times")
