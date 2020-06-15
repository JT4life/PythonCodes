#super() : Used to call base class method

class a:    
    def display(self):
        print("Base class Method ")

class b(a): #b is child of a  
    def display(self):
        super().display()
        print("child class Method ")


class c(b): #c is child of b     
    def display(self):
        super().display()
        print("child of child class Method ")

    
k=c()
k.display()
