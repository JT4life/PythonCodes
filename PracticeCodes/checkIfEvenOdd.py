# Enter a Number,Display The number of digit of That number
# n =456 ---3 | n=8769 ----4
##############

n = int(input("Enter Number"))
c = 0
while n!=0 :
    n=n//10
    c=c+1
print("The Number of Digit is ::",c)

''' Dry Run :::
    
    n=876
    c=0
    --
    n=87     n=8   n=0
    c=1      c=2   c=3
    ---
'''

# Enter a Number , check the number is even or odd ::
n=int(input("Enter Number"))
if n%2==0:
    print("Even Number")
else:
    print("Odd Number")
