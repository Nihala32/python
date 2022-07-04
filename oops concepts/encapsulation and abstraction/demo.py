# encapsulation and abstraction
# wrapping up of data and methods in to a single unit
# restricted access to data and method

# advantages of encapsulation
# it provide well defined readable code
# privents accidential modification or deletion
# security

# public members
# private members

# name mangling: _classname__privatevariablename

class Sample:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def printvalue(self):
        print(self.name,self.__age)
ob=Sample('vinay',25)
ob.printvalue()
print(ob._Sample__age)


