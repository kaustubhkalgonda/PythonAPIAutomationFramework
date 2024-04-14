num1 = 10
num2 = 20

print(num1,num2)
num3 = None
num3=num1
num1=num2
num2=num3

print(num1,num2)

num1,num2 = num2,num1

print(num1,num2)