#Find index of 1st and Last 'O' in "Hello Word"

test_word = "Hollo Wordo"
count = 0
result_list = []
for char in test_word:
    if char == "o":
        result_list.append(count)
    count +=1

print(result_list[0])
print(result_list[len(result_list)-1])