#Inheritence & Method : Method will get called from current class only
#Method : will get called from bottom to top
class a:    
    def display(self):
        print("Base class Method ")

class b(a): #b is child of a  
    def display(self):
        print("child class Method ")


class c(b): #c is child of b     
    def display(self):
        print("child of child class Method ")

    
k=c()
k.display()
