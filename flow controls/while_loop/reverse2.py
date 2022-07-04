# read a number from console and print reverse
num=int(input("enter a number: ")) #123
res=0
while(num!=0):
    dig=num%10
    res=(res*10)+dig
    num=num//10
print(res)

