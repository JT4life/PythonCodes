#Exception Handling
#Types of errors:
'''1.Syntax error,
print"yo"

2.Logical error
using if statement when you are using for loop

3.Run time error (Exception Handling)(execution)
'''
try:
    n = int(input("Enter number"))
    m = int(input("Enter number"))
    result = n / m;
    print("The result is :", result)

except Exception as e:
    print("Error:",e)
finally:#has to execute
    print("Thanks for playing")

#else: will execute only if no error is there
