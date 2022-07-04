# clas person (name,age,place)
# class student (roll,department)

class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    def setstudent(self,roll,department):
        self.roll=roll
        self.dprmnt=department
        print(self.name,self.age,self.place,self.roll,self.dprmnt)
ob=Student()
ob.setperson('vinay',25,'kochi')
ob.setstudent(12,'ABC')