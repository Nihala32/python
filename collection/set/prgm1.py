st={10,12,15,16,20,25,25}

# add function to use a single element

st.add(25)
st.add(100)
print(st)

# update fn used to add multiple fn at a time
st.update([20,52,21])
print(st)


# total sum
# sum=0
# for i in st:
#     sum+=i
# print(sum)

print(sum(st))

print(max(st))
print(min(st))

# len
print(len(st))