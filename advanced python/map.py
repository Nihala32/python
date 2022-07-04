# map

# lst=[1,2,3,4,5,6,7,8,9,10] f(x)==>[1,4,9,16,25,36,49,64,81,100] for entire element in a list
#

# filter
# lst=[1,2,3,4,5,6,7,8,9,10] f(x) ==>[2,4,6,8,10] (if even numbers only) (in a condition)

lst=[1,2,3,4,5,6,7,8,9,10]

# syntax
# variable_name=list(map(arg1,arg2))
# variable_name=list(map(arg1,arg2))

# arg1==>function
# arg2==>iterable

lst=[1,2,3,4,5,6,7,8,9,10]

# def square(num):
#     res=num**2
#     return res

data=list(map(lambda num:num**2,lst))
print(data)

# even numbers only
data=list(filter(lambda num:num%2==0,lst))
print(data)


# [2,3,4,5,6,7,8,9,10,11]
data=list(map(lambda num:num+1,lst))
print(data)

