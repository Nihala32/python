
f=open("numbers","r")
lst=[]
lst_even=[]
lst_odd=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
for i in lst:
    if(i%2==0):
        lst_even.append(i)
    else:
        lst_odd.append(i)
print(lst_even)
print(lst_odd)
print(sum(lst))
print(sum(lst_even))
print(sum(lst_odd))

