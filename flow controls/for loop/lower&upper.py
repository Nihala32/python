num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
even_sum=0
odd_sum=0
for i in range(num1,num2+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)

