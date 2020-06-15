'''1. Exception Handling
2. Use a class and method'''

'''#1. Suppose we have a file, call a.txt with
101,Santosh,,30'00 
102,Sanjay,,400'0
1'03,,Aelene,5000
104,"Tatata",7237

1. read the file
2. clean the file'''

'''class a:
    def write(self):
        try:
            fh=open("A.txt","w")
            nm=["101,Santosh,,30'00","102,Sanjay,,400'0","1'03,,Aelene,5000","104,\"Tatata\",7237"]
            fh.writelines(nm)
            fh.close()
        except Exception as e:
            print("Error = ",e)
    def read(self):
        fh=open("A.txt","r")
        print(fh.read())
    def repl(self):
        fh=open("A.txt","w")
        nm=["101,Santosh,,30'00 ","102,Sanjay,,400'0 ","1'03,,Aelene,5000 ","104,\"Tatata\",7237"]
        nm = [nm.replace(',,',',') for nm in nm]
        nm = [nm.replace('\'','') for nm in nm]
        nm = [nm.replace('\"','') for nm in nm]
        fh.writelines(nm)
        fh=open("A.txt","r")
        print(fh.read())

z = a()
z.write()
z.read()
z.repl()'''


'''#2. List1 :a,b,c,e,f
    List2 :1,2,3,4,5

    output a1 b2 c3 e4 f5'''

'''class b:
    def combine(self):
        try:
            list1=["a","b","c","e","f"]
            list2=[1,2,3,4,5]
            b=[str(x) for x in list2]
            print(list1[0]+b[0])
            print(list1[1]+b[1])
            print(list1[2]+b[2])
            print(list1[3]+b[3])
            print(list1[4]+b[4])
        except Exception as e:
            print("Error = ",e)
z = b()
z.combine()'''

'''#3. List : a,b,c,d
    List2 : b,c,x,y
        1. common output = b c
        2. additional not comment a d x y'''

'''class c:
    def same(self):
        try:
            list1=['a','b','c','d']
            list2=['b','c','x','y']
            res=""
            for i in list1:
                if i in list2 and not i in res:
                    res += i
                    print("intersect is:",i)
                if i not in list2 and i in list1:
                    print("Additionals are:",i)
            for i in list2:
                if i not in list1 and i in list2:
                    print("Additionals are:",i)
        except Exception as e:
            print("error = ",e)

z = c()
z.same()'''
             
            
            

'''#4. Enter a string : count number of vowels (AEIOU)

class d:
    def vow(self):
        try:
            vowels = ["a","e","i","o","u"]
            user = input(str("Enter a word"))
            count = 0
            for i in user:
                if i in vowels and i in user:
                    print("Vowels found ",i)
                    count = count + 1
                else:
                    print("No vowels were found")
            print("Total vowels =",count)
        except Exception as e:
            print("error = ",e)

t = d()
t.vow()'''
                         

'''#5. Matrix :
    123
    456
    789
    display : row total, diagnol total'''


class e:
    def matrix(self):
        try:
            m = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
            sumRows = 0
            for i in range(len(m)):
                for j in range(len(m[i])):
                    sumRows += m[i][j]
            print("Rows total =",sumRows)
            diag = m[0][0]+m[1][1]+m[2][2]+m[0][2]+m[2][0]
            print("Diagonol total =",diag)
        except Exception as e:
            print("Error = ",e)
            
y = e()
y.matrix()
            
