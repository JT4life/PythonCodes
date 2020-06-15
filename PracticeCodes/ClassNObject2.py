#Class and Object

class a:
    #Constructor : Allocates the memory, Just like method | Call automatically, at the time of object creation
    #Used to initialize the attribute of class
    def __init__(self,x=999): #this is how we create constructor in python
        print("Constructor x =",x) 
  
    #Distructor : Releases the memory
    def __del__(self):
        print("Distructor!")
        
    def display(self): #needs to be called
        print("Thanks and welcome!")

z = a();#calls constructor automatically
p = a(333);
z.display();

z.__del__()
print(z)
