lst=[]

# append() fn is used to add a sinlge element to list
lst.append(2)
print(lst)
lst.append(15)
print(lst)
lst.append('luminar')
print(lst)
# lst.append('l',4) not possible
# print(lst)

lst.extend([4,5,6])  #to add multiple elements in a list
print(lst)

lst.insert(1,150)
print(lst)                 #to add a element in a perticular position
lst.insert(4,'big data')
print(lst)
