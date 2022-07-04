# constructor

# used to define instatnce variable in an object
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

pe1=Person("arun",26,"kochi")
pe1.printvalue()

pe2=Person('vinay',25,'calicut')
pe2.printvalue()