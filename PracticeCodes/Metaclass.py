#Python metaclass : a class that instantiates a class
#In python a class is actually an object of another class
#this other class is called Metaclass
#Metaclass in python defines the behaviour of class objects
#type is built in meta class in python

class a():
    pass;

obj=a()
print(type(obj))
print(type(a))

#When we create class, the default metaclass gets called.
#This metaclass contains 1.name of class 2.base class info 3.attributes of class
#Creating class on the fly
student=type('student',(),{})
#student=type('student',(dept,),{})
#class student:
 #   pass
 
#class student(dept):
 #   pass

#class student:
 #   def __init__(self, name, roll):
  #      self.name=name;
   #     self.roll=roll

def init(self, name, roll):
     self.name=name;
     self.roll=roll
student=type('student',(),{'__init__':init})

#We can also create own metaclass
#For this your class must inherit from type
class MyMetaClass(type):
    __metaclass__=type

class a:
    __metaclass__= MyMetaClass

object=a()
print(object.__metaclass__)
print(MyMetaClass.__metaclass__)
