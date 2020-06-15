#String : sequence of char
nm = "Joshua"
nm1 = "Smith"
nm2 = """Allen
            ya
        """
nm3 = '''tata
            asdf
    '''

print(nm)
print(nm1)
print(nm2)
print(nm3)
print(nm[:3]) #Jos

#del nm
print(nm+nm1)
print(nm*3)


s = ("Tata"
     "rara")
print(s)

c = 0
for i in "Hello World":
    if i=="o" :
        c = c + 1
print("No of times o is ", c)
print("n" not in nm)

#Default Order

x="{},{} & {}".format("Santosh","Simon","keen")

print(x)
print(x[0]) #S
print(x[:10]) #Santosh,Si
print(x[4:9]) #osh,S

#Order using positional argument
y="{1},{2} & {0}".format("Santosh","Simon","keen")
y1="{a},{b} & {c}".format(a="Santosh",c="Simon",b="keen")

print(y) #Simon,keen & Santosh
print(y1) #Santosh, keen & Simon

#Escape sequence
print(''' He Said , "What's there?" ''') #He Said , "What's there?"

print('He Said, "What\'s there?" ')

print("She said,\"What\'s there?\"")

print('"She said,\n"What\'s there?\""') #\n new line

#String Function
am="The man of action from earth"
print(am.upper())
print(am.lower())

k=am.split() #split by spaces if not specified
for i in k:
    print(i)

'''k=am.split('a')
for i in k:
    print(i)'''

print(' '.join(k)) #joins string

print("The Legend".find("e")) #e is at index 2, finds first e

print("The Legend".find("e",3)) #finds e after index 3

print("The Legend".replace("e","X"))

#String : Write a program to sort words in Alphabet Order

usrInput=input("Enter a string")
x=usrInput.split()
x.sort()
print(x)

print("the man of action from USA.".capitalize()) #capitalize T

