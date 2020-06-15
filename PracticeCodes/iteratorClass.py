#Iterator class user defined iterator
#Must have iter and next method
#Iterators in python simply an obj that can be iterated upon
#An obj that will return data one element at a time
#Ideally Python iterators must implement __iter__() and __next__()
#Most containers in python : list,tuples,Strings : all are iterables
#Advantage = Save the resources
class a:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=10:
            val=self.num
            self.num+=1
            return val;
        else:
            raise StopIteration

values = a()
print(next(values))

for i in values:
    print(i);
