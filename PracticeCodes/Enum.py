#Python ENumerate
data = ["read","write","speak",234,["xxx","yyy","zzz"]]
eobj=enumerate(data)
for i in eobj:
    print(i)

eobj=enumerate(data,100)
for i in eobj:
    print(i)
