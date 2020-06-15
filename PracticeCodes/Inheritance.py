#Inheritance : single

class a:
    def display(self):
        print("Base class Method")

class b(a): #b is child of a
    def display1(self):
        print("Child class method")
k = b();

k.display();
k.display1();

#multi level inheritance

class c(b):
    def display2(self):
        print("Child of child class method")
d = c()
d.display2();


