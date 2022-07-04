# multiplication table of a given number

number=int(input("enter a number: "))
i=1
while(i<=10):
    res=i*number
    print(i,'*',number,"=",res)
    i+=1