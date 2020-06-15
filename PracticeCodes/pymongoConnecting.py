'''#Display value from connection
from pymongo import MongoClient
conn=MongoClient("localhost",27017) #connect to mongo db port
#Access the database
db=conn.test9.Emp
cur=db.find()
for i in cur:
    print(i["Empno"+" "+i["Ename"]+" "+i["Sal"])

print()
conn.close()'''

'''#How to insert the values
from pymongo import MongoClient
conn=MongoClient("localhost",27017) #connect to mongo db port
#Access the database
db=conn.test9.Emp
#Create Dictionary
emp_rec={}
flag=True
while (flag):
    empno,ename,sal=input("Enter Empno, Ename and Salary(Insert , Separated Value):").split(",")
    emp_rec={"Empno":empno,"Ename":ename,"Sal":sal}
    db.insert(emp_rec)
    flag=input("Enter Another Record(Y/N)?")
    if(flag[0].upper()=="N"):
        flag=False;
#Display values
cur=db.find()
for i in cur:
    print(str(i["Empno"])+" "+i["Ename"]+" "+str(i["Sal"]))
    
print()
conn.close()'''

#How to insert the values directly
from pymongo import MongoClient
conn=MongoClient("localhost",27017) #connect to mongo db port
#Access the database
db=conn.test9.Empl
empl={"_id":101,"Empno":8181,"Ename":"Rarara"}
db.insert_one(empl)
print("Done")

conn.close()
