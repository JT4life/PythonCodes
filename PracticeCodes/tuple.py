#Tuple : Advantage : Faster
a=[11,22,33,4,(22,33,44)]

print(a)

#create tuple without() aka tuple packing
z=11,22,33,"Robin"
print(z)
print(type(z))

#Tuple unpacking
a,b,c,d=z
print(a)
print(b)
print(c)

#How we can create tuple... with single element, need to use ,
t=("joshua",)
print(type(t))

print(z[0])
print(z[-1])

#We can apply +, * with tuple
a=(1,2,3)
b=(4,5,6)
print(a+b)
print(a * 3)

p=[1,2,3]
q=[44,55,66]
print(p+q)

#delete the tuple
'''del a
print(a)'''

#
w=("a","b","b","c","d")
print(w.count("b"))

for i in w:
    print(i)

for j in ("S","G","D"):
    print("Good morning", j)
