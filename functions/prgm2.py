
def qube():
    num=int(input("enter a number: "))
    res=num**3
    print(res)
qube()

def qube(num):
    res=num**3
    print(res)

qube(5)

def qube(num):
    res=num**3
    return res

ans=qube(5)
print(ans)


