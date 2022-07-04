# how to identify an exception
# a=[1,2,3,4]
# i=int(input("enter a range"))
# try:
#     print(a[i])
# except Exception as e:
#     print("exception occured",e)
#
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
try:
    print(num1/num2)
except Exception as e:
    print("error",e)

