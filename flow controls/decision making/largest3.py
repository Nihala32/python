# largest among 3 numer
# 100
# 80
# 60

num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
num3=int(input("enter number3: "))
# if(num1>num2):
#     print("num1 is largest",num1)
# elif(num2>num3):
#     print("num2 is largest",num2)
# else:
#     print("num3 is largest",num3)


if(num1>num2)&(num1>num3):
    print("num1 is largest")
elif(num2>num1)&(num2>num3):
    print("num2 is largest")
else:
    print("num3 is largest")
