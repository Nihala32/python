# employee person
# person =private variable

class Employee:
    def __init__(self,id,name,age,profession):
        self.id=id
        self.fname=name
    def printvalue(self):
        print(self.id,self.fname)
class Person(Employee):
    def __init__(self,place,phn,name,id):
        Employee.__init__(name,id)
        self.place=place
        self.phn=phn
    def printvalue1(self):
        print(self.id,self.fname,self.place,self.phn)

ob=Person(101,'ABC','LLL',2525)
ob.printvalue1()

