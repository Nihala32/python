# exception genarating
age=int(input("enter your age: "))

if age>=18:
    print("you are eligible to vote")
else:
    raise Exception("not allowed")





