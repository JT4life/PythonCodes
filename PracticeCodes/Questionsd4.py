#1. ENTER SOME NUMBER AND DISPLAY THE SUM OF THAT OF NUMBER  
#PROGRAM WILL TERMINATED IF THE NUMBER 0 IS ENTERED
'''
def ans1():
    sum = 0
    n = int(input("Enter number"))
    while n!=0:
        sum = sum + n
        n = int(input("Enter Number"))
    print("Sum is ", sum);

ans1();'''

#2. ENTER A NUMBER , CHECK THE NUMBER PRIME OR COMPOSITE  
#    ---1, ITSELF ... 3,7,17...
'''
def isPrime(n):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1;
            break;
    if flag == 0:
        print("The number is prime ", n)
    else:
        print("The number is composite ", n)

        
isPrime(7)'''        


#3. DISPLAY ALL THE PRIME NUMBER FROM 1 TO 100 , ALSO DISPLAY HOW MANY PRIME NUMEBRS ARE THERE
'''
def prime():
    c = 0
    for n in range(1,101):
        flag = 0
        for i in range(2, n):
            if n % i == 0:
                flag = 1;
                break;
        if flag == 0:
            print("The number is prime", n)
            c = c+1
        else:
            flag = 0;
    print("Number of prime numbers is :", c)

prime()
'''
#4. DISPLAY ALL THE MAGIC NUMBER FROM 1 TO 100  
#        73 --7+3=10  
#        82 --8+2=10 which ever number add equals 10
'''
def magic():
    for i in range(19,100,9):
        print(i)

def magic(n):
    sum = 0;
    while n!=0:
        d=n%10;
        sum = sum + d;
        n = n // 10;
    if sum == 10:
        print("its a magic number! ")

magic(19)
'''
#5. ENTER A NUMBER DISPLAY THE REVERSE OF THAT NUMBER  

def reverseNum():
    userIn = int(input("Enter at least 3 numbers"))
    if userIn >= 3:
        first = userIn % 10;
        second = userIn % 10;
        third = userIn % 10;
        result = str(first) + str(second) + str(third);

        print(result);
#call
reverseNum();
