#WAP , Input = Name , Output = Nxmx

input_word=input("Enter input word: ")
string_list = list(input_word)
output_list = []

for char in string_list:
    if char in ('a','e','i','o','u'):
        output_list.append('x')
    else:
        output_list.append(char)


print(f"Output word is: {"".join(output_list)}")