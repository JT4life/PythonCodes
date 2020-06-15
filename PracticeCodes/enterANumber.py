#Enter a number display the number of digit of that number
# n=456 ----3 | n=8769 ----4

n = int(input("Enter a number"))
c = 0
while n!=0:
    n=n//10
    c=c+1
print("The number of the digit is :",c)

'''#Dry Run:

n=876
c=0
---
n=87  n=8  n=0
c=1   c=2  c=3
---
'''

#Enter a number, check the number is even or odd
n=int(input("Enter a number"))
if n%2==0:
    print("Even Number")
else:
    print("Odd number")
    
