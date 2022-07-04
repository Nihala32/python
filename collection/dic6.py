# each location count
f=open("C:/Users/amina/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    loc=data[-1]
    if loc  not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
print(dic)

