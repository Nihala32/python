# static variable
# here clg name can set as a static variable


class Student:
    clg_name='ABC'
    def setvalue(self,name,age,rollnu):
        self.name=name
        self.age=age
        self.roll=rollnu
    def printvalue(self):
        print(self.name,self.age,self.roll,Student.clg_name)

st1=Student()
st1.setvalue('vinay',25,11)
st1.printvalue()

st2=Student()
st2.setvalue('nihala',21,12)
st2.printvalue()


