# qstn6
lower_limit=int(input("enter lower limit: "))
upper_limit=int(input("enter upper limit"))
even=0
odd=0
for i in range(lower_limit,upper_limit+1):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)
