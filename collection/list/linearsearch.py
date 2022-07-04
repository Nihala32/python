lst=[1,5,7,8,3,6,2,9,15,20]
# read a element from console
# element found &element not found
#
# num=int(input("enter a number: "))
# if num in lst:
#         print("element found")
# else:
#     print("element not found")
#


# linear search
num=int(input("enter a number: "))
flag=0
for i in lst:
    if(num==i):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")
# limitation
# 1.increase complexity


