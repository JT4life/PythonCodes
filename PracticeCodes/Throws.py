#Throws, to raise an error
#try:
a = int(input("Enter number"))
print(a)
if a > 100:
    raise NameError("Value > 100 not allowed") #the class for user error
#except NameError as e:
#    print(e)
#try and except not required when using raise(throw)
