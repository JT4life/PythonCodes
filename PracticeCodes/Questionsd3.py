#appending
'''
>>> m=[11,22,33,44,55]  
>>> print(sum(m))  
165  
>>> print(sum(m)/5)  
33.0  
>>> p=[]  
>>> p.append(22)  
>>> p.append(33)  
>>> p.append(12)  
>>> p.append(2)  
>>> print(p)  
[22, 33, 12, 2]  
>>> p.sort()  
>>> print(p)  
[2, 12, 22, 33]  
>>>'''

#1 Suppose We are having List, Need to find All Even Number and all Odd number
# in Different-2 list, Finally display sum of that
a=[1,2,3,44,63]

even=[]
odd=[]

for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


#2 We are having 2 list ... merge the list and display in sorted order
c=[5,2,3,4]
d=[5,6,7,8]
e = c+d
list.sort(e)

print(e)

#3 We are having List of 5 different number .. Display max and min value
five = [5,3,2,6,8]

print(min(five))
print(max(five))

## 1. We are having 2 variables..with some values ... Swap the values ... Without using 3rd variable
a = 5;
b = 3;

a = a + b;
b = a - b;
a = a - b;
print(b)
print(a)



## 2. Display all the possible combination of 3 Numbers : [2,3,4]
intArr = [2,3,4];

