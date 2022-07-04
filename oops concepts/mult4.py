# person name,age
# child place,school
# student roll no department clg
# print name age place departmnt clg

class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setchild(self,place,school):
        self.place=place
        self.school=school
class Student(Child):
    def setstudent(self,roll,department,clg):
        self.r=roll
        self.d=department
        self.c=clg
    def printstud(self):
        print(self.name,self.age,self.place,self.d,self.c)

ob=Student()
ob.setperson('vinay',25)
ob.setchild('clt','nnm')
ob.setstudent(11,'science','abc')
ob.printstud()