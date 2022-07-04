
# class Person: name,age,place
# student roll nu,departmnt.clg

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.clg=place
        print(self.name,self.age,self.clg)
class Student(Person):
    def __init__(self,rollnumber,department,college,name,age,place):
        super().__init__(name,age,place)
        self.roll=rollnumber
        self.department=department
        self.clg=college
    def printstud(self):
        print(self.roll,self.department,self.clg)
ob=Student('vinay',26,'kochi',101,'bigdata','abc')
ob.printstud()
