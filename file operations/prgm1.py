
f=open("numbers","r")
lst=[]


for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)




# rstrip
#
# line="hello/n"
#
# data=line.rstrip("0/n")
# print(data)







