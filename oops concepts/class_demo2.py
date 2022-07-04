class Person():
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)

pe1=Person()
pe1.setvalue('nihala',21,'kozhikode')
pe1.printvalue()

pe2=Person()
pe2.setvalue('arjun',25,'malappuram')
pe2.printvalue()

pe3=Person()
pe3.setvalue('ansi',22,'kochi')
pe3.printvalue()

# name
# age
# place
# self arguments(global arguments)


