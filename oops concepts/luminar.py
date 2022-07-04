# class luminar argmnts name,roll,age,institution name,fees

class Luminar:
    institution_name='Luminar'
    fees=29000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.institution_name,Luminar.fees)

lu1=Luminar()
lu1.setvalue('nihala',2,21)
lu1.printvalue()

lu2=Luminar()
lu2.setvalue('ansiba',3,22)
lu2.printvalue()

lu3=Luminar()
lu3.setvalue('nesri',4,22)
lu3.printvalue()
