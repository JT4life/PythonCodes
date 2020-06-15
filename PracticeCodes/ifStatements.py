c=int(input("Enter a number"))

if c < 50:
    print("C is less than 50")
else:
    print("C is greater than 50")
    
if c < 100:
    print("C is less than 100")
elif c > 100 and c < 200:
    print("C is greater than 100 and less than 200")
else:
    print("C is", c)

