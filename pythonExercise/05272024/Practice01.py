#Remove Duplicate from a List

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

result_list=[]

for ele in test_list:
    if ele not in result_list:
        result_list.append(ele)


print(f"Result list is: {result_list}")