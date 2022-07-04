# multilevel inheritance

class A:
    def seta(self):
        print("inside class a")
class B(A):
    def setb(self):
        print("inside class b")
class C(B):
    def setc(self):
        print("inside class c")

ob=C()
ob.setc()
ob.setb()
ob.seta()