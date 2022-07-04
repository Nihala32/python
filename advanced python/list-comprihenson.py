# list-comprihenson

# empty list
# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)

# syntax
# lst=[print range]

lst=[i for i in range(1,101)]
print(lst)

# 1 to 75
lst=[i for i in range(1,76)]
print(lst)

lst=[i for i in range(1,76,4)]
print(lst)

# from 1 to 100 print even numbers only
# lst=[print range condition]
lst=[i for i in range(1,101) if i%2==0]
print(lst)

# 1 to 50 print odd numbers
lst=[i for i in range(1,51) if i%2!=0]
print(lst)

# num even print even
lst=[(i,'even') for i in range(1,51) if i%2==0]
print(lst)

# syntax (more than one condition)
# lst=[print if conditon1 else print2 if  condition2 else print3  range]

# 1 to 50 print sqr if even else print qb
lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

lst=[(i**2) if i%2==0 else i**3 for i in range(1,51)]
print(lst)


# if even sqr else print number
lst=[(i,i**2) if i%2==0  else i for i in range(1,51)]
print(lst)


# if num even print even else print odd
lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,31)]
print(lst)

# num even sqr num 5 div print 0 else i
lst=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,16)]
print(lst)

name="luminartechnolab"
v="aeiou"
# print vowels
lst=[i for i in name if i in v]
print(lst)



lst=["y" if i in v else "n" for i in name]
print(lst)








