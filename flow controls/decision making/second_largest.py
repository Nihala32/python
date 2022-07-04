# read 3 numbers from console and find the second largest number (nested if)

num1=int(input("first number: "))
num2=int(input("second number: "))
num3=int(input("third number: "))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("num2 is second largest")
    else:
        print("num3 is second largest")
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print("num1 is second largest")
    else:
        print("num3 is second largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largest is num1")
    else:
        print("num2 is second largest")
else:
    print('invalid input')