##Set :: Unordered Collection of Unique Items
# {}

m={11,11,22,22,33,44,44,44,55}
print(m)

m1={11,11,"tata",(11,11,11,22,22,22)}
print(m1)

m2={11,11,"RARA",11,11,11,22,22,22}
print(m2)

a=[11,22,33,33,44,44,55]
print(set(a))

b={} #Dictionary type
print(type(b))

c=set()
print(type(c))

c.add(2) #Single value we can use add
c.add(34)
print(c)

c.update([2,3,5]) #Multiple values we use update
print(c)

c.update([2,3,5],["yaya","tata","usus"])
print(c)

#Remove
c.discard(3)
print(c)

c.remove(2)
print(c)

c.discard(324) #nothing happens
print(c)

c.pop() #remove first item from beginning index
print(c)

c.clear() #Clear removes all items
print(c)

ab={11,22,33,44}
bc={22,33,55,66}

#Union
print(ab|bc)
print(ab.union(bc))

#Intersection
print(ab & bc)
print(ab.intersection(bc))

#Difference minus unique of first
print(ab-bc) # only 11 and 44 are left
print(ab.difference(bc))

#Symmetric Difference
print(ab ^ bc)
print(ab.symmetric_difference(bc))
