#Q: 1. ENTER A NUMBER DISPLAY THE TABLE OF THAT NUMBER
a=int(input("Enter a number"))

for i in range(1,11):
    print(a*i)

#2. DISPLAY REVERSE OF ANY GIVEN NUMBER
'''b=int(input("Enter a number to reverse"))

Reverse = 0
while(b > 0):
    remainder = b %10
    Reverse = (Reverse *10) + remainder
    b = b //10
    print("Reverse of number is = %d" %Reverse)'''

n=int(input("Enter number"))
while (n!=0):
    b=n%10
    print(b)
    n=n//10
'''Dry Run::
n=789
---
b=9  b=8  b=7
n=78 n=7  n=0
'''

#2.5 Display in reverse
n=int(input("Enter number"))
r=0
while (n!=0):
    b=n%10
    r=r*10+b
    n=n//10
print(r)

'''Dry run:
n=876
r=0
b=6  b=7   b=8
r=6  r=67  r=678
n=87 n=8   n=0
'''

#3. DISPLAY FACTORIAL OF ANY GIVEN NUMBER
factNum=int(input("Enter a number to factorial"))
fact=1

for i in range(1,factNum+1):
    fact = fact * i
print("factorial is",fact)

'''dry run
n=5
i=1    i=2      i=3     i=4      i=5
fact=1 fact=2 fact=30  fact=24   120
'''



