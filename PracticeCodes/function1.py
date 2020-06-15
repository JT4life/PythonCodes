#Function
#Subprogramming For modular approach

def display():
    print("Hello function")

def display1(nm):
    print("Thanks and welcome ::",nm)

def sum(x,y):
    return x+y

def display3(x,y):
    print("x=",x," ","y=",y)

def display4(x,y=8): #default argument must be last
    z=x+y
    print("z=",z);

def display5(x=3,y=6):
    z=x+y
    print("z=",z)

def display6(*z): #arbitary argument can put n number of values
    for i in range(0,len(z)):
        print(z[i])
    
#Call
display()
display1("hello parameter")

#Sum
t=sum(4,6)
print(t)
'''
display3(44,55)
display4(55)
display5()
display5(5)'''
display6(33,44,55,66,77)
display6("aaa","ggg",555)
