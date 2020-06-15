a=[22,33,44,"joshua",4.5,"thao",666]

print(a[3])
print(a[-1])

#List is mutable and ordered sequence

a[0]="Allen"
print(a[0])

#Tuple same as list, but is immutable use ()

n=(11,22,33,44,"ss",5.6,44,22)
print(type(n))

print(n[-1])

print(n[2:5])

#Python String : sequence of char, for string
#start index at 0
#like tuple its immutable

nm="joshua is at the park"
print(nm)

ab=""" abcd pqr """
print(ab[0:5])

#Set immutable, unordered collection of unique items no dups
st={"aa","aa","aaa","aaa",22,22,33,44,55,22,22,11}
print(type(st))

#tuple, string, set are immutable
#list, tuple, string can use index its not allow in set
#advantage of set is unique items
#list : [], tuple : (), set : {}
#Python dictionary :: its an unordered collection of key value pairs
m = {"Name":"Joshua","Subject":"Python"}
print(m)

print(type(m))

print(m["Name"])


