#Iterator
m=[22,33,44,55,66]
print(m[0])
#iter and next

it=iter(m)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
#print(it.__next__()) causes exception stop iteration no more to iter

for i in m:
    print(i)

it = iter(m)
print(it.__next__())
print(it.__next__())
