#Dictionary : unorder collection of items Key/Value pairs
#To create use {}
#Empty Dict
#myDic = {}
#      Key Value
dic1 = {1:"Joshua","2":"Z"}

dic2 = {"Name":"Santosh", 1:[1,2,3,4]}

dic3 = dict({1:'ABCD',2:'XYZ'})

#How to access values

print(dic1[1])
print(dic2["Name"])
print(dic3[1])

#Changes : Its mutable we can add/change values

dic1={1:"Adam from USA"}

print(dic1[1])
print(dic2.get("Name"))

dic1["Address"] = "India"
print(dic1["Address"])

#Remove or Delete : pop() To remove particular items
#Clear : Removes all items || Pop item remove arbitary item
print(dic1)
print(dic1.pop("Address"))
#dic1.clear()
print(dic1)

print(dic2.popitem())
print(dic2)

#delete
    #Value number
del(dic3[1])
print(dic3)

for i in dic1:
    print(dic1[i])

print(len(dic1))
a = {9:"aaa",4:"ttt",2:"yyyy"}
print(sorted(a))
    
