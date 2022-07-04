# polymorphism

# many character

# in methods
# method overloading    dfrnce in number of argmnts
class A:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class B(A):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

ob=B()
ob.sum(1,6,3)
# ob.sum(1,4)


