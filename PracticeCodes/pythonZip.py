#Python Zip : Its a container, that holds the real data inside
test=zip()
print("Type of empty ZIP",type(test))

list1=['aaa','bbb','ccc','ddd']
list2=['one','two','three','four']

test=zip(list1,list2)
print("The zip values are :")
for i in test:
    print(i)

testlist=list(zip)
a,b=zip(*testlist)
print(a)
print(b)
