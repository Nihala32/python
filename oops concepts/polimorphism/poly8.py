lst=[]
class Employee:
    def __init__(self,id,first_name,last_name,age,profession,location):
        self.id=id
        self.fname=first_name
        self.lname=last_name
        self.age=age
        self.pro=profession
        self.loc=location
    def printemployee(self):
        print(self.id,self.fname,self.lname,self.age,self.pro,self.loc)
f=open("C:/Users/amina/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    first_name=data[1]
    last_name=data[2]
    age=data[3]
    profession=data[4]
    location=data[-1]
    ob=Employee(id,first_name,last_name,age,profession,location)
    # ob.printemployee()

    lst.append(data[1:5])
print(lst)