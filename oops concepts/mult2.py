# class person name,age
# class parent place phone number
# class employee id designation salary
# print name,age,place phone id designation salary

class Person:
    def setvalue1(self,name,age):
        self.n=name
        self.a=age

class Parent:
    def setvalue2(self,place,phone):
        self.p=place
        self.ph=phone

class Employee(Person,Parent):
    def setvalue3(self,id,designation,salary):
        self.i=id
        self.ds=designation
        self.sly=salary
    def printemployee(self):
        print(self.n,self.a,self.p,self.ph,self.i,self.ds,self.sly)

ob=Employee()
ob.setvalue1("nihala",21)
ob.setvalue2("calicut",252525)
ob.setvalue3(11,"python",1500)
ob.printemployee()