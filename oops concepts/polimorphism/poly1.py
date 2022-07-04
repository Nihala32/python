# method  over riding
# same method name and number of argmnts
# python does'nt support over loading but support over riding

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("class a",self.num1+self.num2)

class Add2(Add):
    def sum(self,no1,no2):
        self.num1=no1
        self.num2=no2
        print("class b",self.num1+self.num2)

ob=Add2()
ob.sum(15,20)
