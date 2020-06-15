#Pyhton Command Line Argumnet
import sys
print(type(sys.argv))
print("Highest and Lowest are :")

for i in sys.argv:
    print(min(i),max(i))

for i in sys.argv:
    print(5+4)
