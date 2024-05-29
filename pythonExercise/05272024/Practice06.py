# region Description
#Pattern-
1
12
123
1234
12345
# endregion

count = int(input("Enter number of rows to be printed: "))

for i in range(1, count+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()