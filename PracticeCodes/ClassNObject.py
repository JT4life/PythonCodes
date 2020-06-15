#Class and object in python

'''class a:
    def display(self):
        self.x = 100    #public attr
        self.y = 200    #public attr
        z=999           #private attribute
        print("The first example of class and object", self.x,self.y)
    def display2(self):
        print(self.x)

#Object
    
k = a() #K is object of class a

#Call the methods of class : objectname.methodname()
k.display()

print(k.x," ",k.y," ")

k.display2()'''

#2nd example how to pass parameters
'''class a:
    def display(self,p,q):
        self.x=p  
        self.y=q
        print("The First Example of class and Object-->",self.x,self.y)
    
#Object
k=a()
a=int(input("Enter Number"))
b=int(input("Enter Number"))
k.display(a,b)'''

#3rd method overloading
class a:
    def sum(self,p,q=100):
        print(p+q)

#call
k = a()
k.sum(22,33)
k.sum(22) #if you pass only 1 parameter than it adds the default 100
k.sum("a","b") # prints ab, automatically converts to string
k.sum(2.3,5.6)
