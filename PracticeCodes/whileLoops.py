#While loops
i=0
while (i <= 5):
    i = i +1
    print(i)
    

while (i <=10):
    i=i+1
    print(i)
else:
    print("Welcome")

for i in range(1,11):
    if i==5:
        continue; #skip 5
    print(i)
    

for i in range(1,11):
    if i==5:
        break; #exit the for loop when it reaches 5
    print(i)


