#Inheritence & Constructor
# How the constructor will get called : Constr will get call from current class so c
#In Java | C# | C++ : Constr will be call from top to bottom
class a:
    def __init__(self):
        print("a class constructor")
        
    def display(self):
        print("Base class Method ")

class b(a): #b is child of a
    def __init__(self):
        print("b class constructor")
        
    def display1(self):
        print("child class Method ")


class c(b): #c is child of b
    def __init__(self):
        print("c class constructor")
        
    def display2(self):
        print("child of child class Method ")

    
k=c()
k.display()
k.display1()
k.display2()
