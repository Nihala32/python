
def binary(lst,key):
    low=0
    end=len(lst)-1
    mid=0
    while(low<=end):
        mid=(low+end)//2
        if(lst[mid]<key):
            low=mid+1
        elif(lst[mid]>key):
            end=mid-1
        else:
            return mid
    return -1
r=binary([5,7,9,13,32,33,42,54,56,58],7)
if(r==-1):
    print("not found")
else:
    print("found")
