#Inheritence :Hybrid

class a:
    def display(self):
        print("Base class Method ")

class b: 
    def display1(self):
        print("child class Method ")

class c(a,b):  #c is child of both a and b
    def display2(self):
        print("child of child class Method ")

class d(c):
    def display3(self):
        print("Hybrid Inheritnce demo")
    
k=d()
k.display()
k.display1()
k.display2()
k.display3()
