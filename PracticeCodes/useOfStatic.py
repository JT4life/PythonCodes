#Static keyword in Java not in python. If we need to declare static attribute
#How to do that?

class a:
    t=100 #this is the static attribute
    def display(self):
        print("Base class Method t =",a.t)

k=a()
k.display()
print(a.t) # a.t to call the static attribute
print(k.t) # can all using k as well
