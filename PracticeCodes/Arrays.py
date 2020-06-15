#Array : In python we dont have Native Array, use list instead
m = [11,22,33,55,77]
print(m)
print(m[0])

m1 = [[1,2],[3,4],[7,8]]
print(m1)
print(m1[1][1]) #prints 4

#Matrix : 2 Dimensional data Structure
a = [[11,22,33],[34,45,55],[55,66,77]]
print(a)

#1. Display Row Total
arr = [[11, 22, 33],
      [33, 44, 55],
      [55, 99, 88]]

rows = print(len(arr))

#2. Display Column Total

columns = print(len(arr[0]))

#3. Diagnol Total

total = print(arr[0][0]+ arr[1][1] + arr[2][2])

#4. String : Allen Smith Border --> Display A.S.Border | Border Smith Allen
# | B.S.A

name="Allen Smith Border"

allen = name[0:5].replace("Allen","A.")
smith = name[6:11].replace("Smith","S.")
bord = name[11:18].replace("Border","B.")
border = name[11:18]
print(allen+smith+border)

print(name[11:18]+" "+name[6:11]+" "+name[0:5])

print(bord+smith+allen)

#5. String : AbCd --> aBcD lower to uppper and vice versa

string1 = "AbCd"

empty =""

for i in range(len(string1)):
    if string1[i].islower():
        empty=string1[i].upper();
    if string1[i].isupper():
        empty=string1[i].lower();
    print(empty)



