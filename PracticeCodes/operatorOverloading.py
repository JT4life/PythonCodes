#Operator Overloading

'''3+4 = 7
"A"+"b"=Ab
 |   |
 Operand

 + : Operator'''

'''a=10
b=20
print(a+b)
print(int.__add__(a,b))
print(a-b)
print(int.__sub__(a,b))
a="tatat"
b="batata"
print(a+b)
print(str.__add__(a,b))'''

class a:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):#Override the add operator
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        y = a(m1,m2)
        return y;
    def __gt__(self, other):#greater than override
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):#override the str method
        return self.m1,self.m2

    
z = a(100,44)
x = a(55,66)
y = z+x
print(y.m1," ",y.m2)
print(z.m1," ",z.m2)

if z > x:
    print("z is greater and won")
else:
    print("x won")

a=10
print(a.__str__())
print(z.__str__())
