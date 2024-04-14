num=17

if num>1:
    for i in range(2,num):
        if num%i == 0:
            print("Not a prime number")
            exit()
    print("Prime Number.")
else:
    print("Enter number greater than 1")