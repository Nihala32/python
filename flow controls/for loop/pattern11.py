# read lower and upper from console,print prime numbers b/w them

lower=int(input("enter first num1: "))
upper=int(input("enter num2: "))
for num in range(lower,upper+1):
    for i in range(2,num):
        if(num%i==0):
          break
    else:
        print(num)