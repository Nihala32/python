
# create a calc
# 1.addition
# 2.substraction
# 3.multiplication
# 4.division

# enter your choice
# num1
# num2
# answer

def add(num1,num2):
    sum=num1+num2
    print(sum)

def sub(num1,num2):
    res=num1-num2
    print(res)

def mult(num1,num2):
    res=num1*num2
    print(res)

def div(num1,num2):
    res=num1/num2
    print(res)

print("1.addition\n2.substraction\n3.multiplication\n4.division\n"
        )
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
choice=int(input("enter your choice: "))

if(choice==1):
    add(num1,num2)
elif(choice==2):
    sub(num1,num2)
elif(choice==3):
    mult(num1, num2)
elif(choice==4):
    div(num1,num2)
else:
    print("invalid")

