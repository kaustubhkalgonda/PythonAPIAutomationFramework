#Reverse a List

test_list=[1, 3, 5, 6, 3, 5, 6, 1]
result_list=[]

for i in range(-1,-(len(test_list))-1,-1):
    result_list.append(test_list[i])

print(result_list)
print(result_list[::-1])