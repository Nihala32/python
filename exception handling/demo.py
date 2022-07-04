# num1=int(input("enter num1:"))
# num2=int(input("enter num2"))
# print(num1/num2)


# ex:6/0
# exception handing errors
# errors depended on input

# 3 blocks are used to handle the exception
# 1.try block
# 2,except block
# 3.finally block

# try block - add the exception code
# except-add solution of the exception code
num1=int(input("enter num1:"))
num2=int(input("enter num2"))
try:
    print(num1/num2)
except:
    print("zero division error")
finally:
    print("mm")





