# read  lower and upper and add sum of even numbers and odd numbers

lower_lmt=int(input("enter lowerlimit: "))
upper_lmt=int(input("enter upperlimit: "))
sum_even=0
sum_odd=0
while(lower_lmt<=upper_lmt):
    if(lower_lmt%2==0):
        sum_even+=lower_lmt
    else:
        sum_odd+= lower_lmt
    lower_lmt+=1
print(sum_even)
print(sum_odd)