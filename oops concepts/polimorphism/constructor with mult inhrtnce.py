
# class person name,age,place
# class employee id,dprmnt,salary
# class student roll,clg

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee:
    def __init__(self,place,phn):
        self.place=place
        self.phn=phn
class Student(Person,Employee):
    def __init__(self,name,age,place,phn,roll,clg):
        Person.__init__(self,name,age)    #imp
        Employee.__init__(self,place,phn)
        self.roll=roll
        self.clg=clg
    def printstud(self):
        print(self.name,self.age,self.place,self.phn,self.roll,self.clg)

ob=Student('vinay',25,'kochi',1212,1,'ab')
ob.printstud()



