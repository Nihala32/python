lst=[3,5,4,1,7,8,55,11]
lst.sort()
num=int(input("enter a number: "))
low=0
upper=len(lst)-1
flag=0
while(low<=upper):
    mid=(low+upper)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upper=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("not found")




