
# factorial

def fact():
    number=int(input("enter number: "))
    sum=1
    for i in range(1,number+1):
        sum=i*sum
    print(sum)
fact()

def fact(num1):
    sum=1
    for i in range(1,num1+1):
        sum=i*sum
    print(sum)

fact(5)

def fact(num):
    sum=1
    for i in range(1,num+1):
        sum=i*sum
    return sum

answer=fact(5)

print(answer)

