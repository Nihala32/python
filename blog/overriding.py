class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs

class Pycharm(Ide):

    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("debud")
        funcs.append("exicute")
        return funcs

class Vccode(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs

py=Pycharm()
print(py.functionalities())

vs=Vccode()
print(vs.functionalities())