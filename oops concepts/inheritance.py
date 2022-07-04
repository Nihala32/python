# inheritance

# parent class, base class, super class
# child class, sub class, derived class

class A:
    def printa(self,num1):
        self.num=num1
        print("inside class A", self.num)

class B(A):
    def printb(self,num2):
        self.num2=num2
        print("inside class b",self.num2,self.num)
a=B()
a.printa(15)
a.printb(42)

