# tuples

# 1.how to define
tu=()   #using paranthesis
print(type(tu))
tu1=tuple()
tu=(1,2,3,4,5,6,7)
print(tu)
# 2.hetrogenous supported or not
tu1=(10,10.5,'pyuthon',True)
print(tu1)

# 3.duplicate value allowed or not
tu2=(1,1,2,4,5,8,7,7,9,5)
print(tu2)

# 4.insertion order preserved

# tuple are immutable
tu2[3]=100
print(tu2)