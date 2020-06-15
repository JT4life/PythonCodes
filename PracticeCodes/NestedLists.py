#List :: []
#Empty list
myList=[]
myList1=[1,2,3]
myList2=[1,"Hi",3.5]

#Nested list
myList3=["A","b",[22,33,44,55],"T","C"]


#List index

print(myList3[0])
print(myList3[2][2]) # prints 44 from position 2
#print(myList3[1.0]) error floats wont work
print(myList3[-1]) # last index

#Slice list in python
print(myList3[1:2])

m=[1,2,3,4,5]

print(sum(m))
print(len(m))

