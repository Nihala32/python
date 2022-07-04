cost=int(input("enter the cost price: "))
if(cost>100000):
    print("tax: ",cost*15/100)
elif(50000<=cost>100000):
    print("tax: ",cost*10/100)
else:
    print("tax: ",cost*5/100)

