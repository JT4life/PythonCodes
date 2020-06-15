#2000-3200 which are divisible by 7 but not 5
'''l=[]
for i in range(2000, 3201):
    if (i%7 == 0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))'''


#Compute factorial of given numbers
'''def fact(x):
    if x == 0:
        return 1
    return x * fact(x -1)

print(fact(4))
x=int(input())
print (fact(x))'''

#With a given integral number n, write a program to generate a
#dictionary that contains (i, i*i) such that is an
#integral number between 1 and n (both included).
#and then the program should print the dictionary.
'''n=int(input())
d=dict()
for i in range(1, n+1):
    d[i]=i*i
print(d)'''
    
#Write a program which accepts a sequence of comma-separated numbers
#from console and generate a list and a tuple which contains every number.
'''
n=input()
l=n.split(",")
t=tuple(l)
print(l)
print(t)'''

'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class InputOutString(object):
    def __init__(self):
        self.s = ""


    def getString(self):
        self.s = input()


    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()

        
