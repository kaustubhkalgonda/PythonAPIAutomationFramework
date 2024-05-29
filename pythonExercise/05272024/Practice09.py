# two Sum problem
# array = [1 , 4 , 5 , 11 , 12]
# target = 9

input_list = [1, 4, 8, 11, 12]
target = 9

for num in input_list:
    for j in range(1, len(input_list)):
        if num + input_list[j] == target:
            print("target found.")
            print(f"{num} and {input_list[j]}")
            exit()
print("Target not found.")
