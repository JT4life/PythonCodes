#Generators : It gives iterators
#Dont need to use iter or next
#Function with yield is generator function
#return .. exit from function, in case of yield..its temporary
#The values will be preserve between calls
def a():
    yield 1
    yield 2
    yield 3
    yield 4

values = a()
print(next(values))
for i in values:
    print(i)

'''def topTen():
    n=1
    while n <=10:
        sq = n*n
        yield sq
        n+=1

values = topTen()
for i in values:
    print(i)'''
