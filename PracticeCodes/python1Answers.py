#1. ENTER A NUMBER DISPLAY SUM OF EACH DIGIT OF NUMBER
a=int(input("Enter a number to add"))
b=int(input("Enter another number"))
c=a+b
print("Sum of both numbers are ",c)

#2. ENTER A NUMBER DISPLAY SUM OF EACH EVEN DIGIT OF NUMBER
num=int(input("2. Enter a number"))

if num % 2 == 0:
    print(num + num,"sum is an even number")
else:
    print(num,"is not an even number")

#3. ENTER A NUMBER DISPLAY THE NUMBER IS PAL IN DROME OR NOT
#        111 ---111 | 121 ---121 |313 ---PAL IN DROME

isPal=int(input("3. Enter 3 numbers to check if it's palindrome"))

sum = 0
r = 0
temp = isPal
while (isPal > 0):
    r = isPal % 10;   
    sum = (sum*10)+r;    
    isPal = isPal/10;

if sum == temp:
    print("numbers are palindrome ",isPal)
else:
    print("numbers are not palindrome ",isPal)
#4. ENTER A NUMBER CHECK THE NUMBER IS EVEN DIGITED OR ODD DIGITED
#        124 -- 3 --ODD DIGITED NUMBER
#        1233 -- 4 --EVEN DIGITED NUMBER
numEnter=int(input("4. Enter a number to see if its even or odd digited"))

if numEnter % 2 == 0:
    print("number is even digited ",numEnter)
else:
    print("number is odd digited ",numEnter)
        
#5. ENTER A NUMBER CHECK THE NUMBER PERFECT NUMBER OR NOT
#       6 ---1,2,3 ---6
#       28 --1,2,4,7,14 ---28
