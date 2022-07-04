# check given number is prime or not
# 2,3,5,7,11,13

num = int(input("Enter a number: "))
flag=0
for i in range(2, num):
         if (num % i) == 0:
           flag=1
           break
if(flag>0):
    print(num,"is not a prime number")
else:
    print(' prime number')




