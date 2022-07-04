# single  parent class=1 child class=1
# multiple: parent = more than one parent class=1

class A:
    def printa(self):
        print("inside class a")
class B:
    def printb(self):
        print("inside class b")
class C(A,B):
    def printc(self):
        print("inside class c")
ob=C()
ob.printb()
ob.printa()
ob.printc()


