# student
# name,rollnum,deprtmnt,clg_name
# create object of 3 students

class Student():
    def setvalue(self,name,rollnum,dprtmnt,clg_name):
        self.name=name
        self.rollnum=rollnum
        self.dprtmnt=dprtmnt
        self.clg_name=clg_name
    def printvalue(self):
        print(self.name)
        print(self.rollnum)
        print(self.dprtmnt)
        print(self.clg_name)

pe1=Student()
pe1.setvalue('nihala',12,'bca','sias')
pe1.printvalue()

pe2=Student()
pe2.setvalue('ansi',11,'cs','sias')
pe2.printvalue()

pe3=Student()
pe3.setvalue('nasri',24,'bca','sias')
pe3.printvalue()
