'''from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Emp
cur=db.find()
for i in cur:
    print(str(i["Empno"])+" "+i["Ename"]+" "+str(i["Sal"]))

print()
conn.close()'''

from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Empl
# Create Dictionary
emp_rec={}
flag=True
while (flag):
    empno,ename,sal=input("Enter Empno,Ename and Salary(Insert , Seprated Value):").split(",")
    emp_rec={"Empno":empno,"Ename":ename,"Sal":sal}
    db.insert(emp_rec)
    flag=input("Enter Another Recurd(Y/N)?")
    if(flag[0].upper()=="N"):
        flag=False;

#Display Values:
cur=db.find()
for i in cur:
    print(str(i["Empno"])+" "+i["Ename"]+" "+str(i["Sal"]))
print()
conn.close()

'''#HOW TO INSERT THE VALUE  
#1
from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Empl
empl={"_id":103,"Empno":9999,"Ename":"JTJTJTJ"}
db.insert_one(empl)
print("Done")
conn.close()'''
