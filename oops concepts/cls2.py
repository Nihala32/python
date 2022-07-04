# class employee
# name,id,designation,salary,company

class Empoyee:
    def setvalue(self,name,id,designation,salary,company):
        self.name=name
        self.id=id
        self.dsgntn=designation
        self.slry=salary
        self.cmpy=company
    def printvalue(self):
        print(self.name,self.id,self.dsgntn,self.slry,self.cmpy)

pe1=Empoyee()
pe1.setvalue('vinay',112,'developer',1500,'tcs')
pe1.printvalue()

pe2=Empoyee()
pe2.setvalue('abina',111,'testing',5000,'abc')
pe2.printvalue()