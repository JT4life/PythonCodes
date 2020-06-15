#1. Operator Overloding >

class a:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False

z = a(100,44)
x = a(60,30)
print(z>x)
print(z.m1," ",z.m2)


#2. Write program for Iterator , Generator and Decorater



#3. Create a class with constr,methods and global variable


