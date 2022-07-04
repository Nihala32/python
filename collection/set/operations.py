# set operations
# 1.union
# 2.intersection
# 3.diffrence


# 1.union
st1={1,2,3,4,5,6,7,8,9,10}
st2={7,8,9,10,11,12,13,14,15}

st3=st1.union(st2)
print(st3)

# 2.intersection
st1={1,2,3,4,5,6,7,8,9,10}
st2={7,8,9,10,11,12,13,14,15}

st3=st1.intersection(st2)
print(st3)

# 3.diffrence

# A-B (element present in a ,not in b
st3=st1.difference(st2)
print(st3)

