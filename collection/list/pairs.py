
lst=[4,3,2,1]
num=int(input("enter a number: "))
lst.sort()
low=0
upper=len(lst)-1
while(low<=upper):
    data=lst[low]+lst[upper]
    if(data==num):
        print("pairs are",lst[low],lst[upper])
        break
    elif(data>num):
        upper=upper-1
    else:
        low=low+1
