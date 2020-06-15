#Delete using pymongo
from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Empl
# Create Dictionary
emp_rec={}
flag=True
while (flag):
    empno = input("Enter Empno to delete")
    emp_rec={"Empno":empno}
    db.delete_one(emp_rec)
    flag=input("Enter Another Recurd(Y/N)?")
    if(flag[0].upper()=="N"):
        flag=False;

#Display Values:
cur=db.find()
for i in cur:
    print(str(i["Empno"])+" "+i["Ename"]+" "+str(i["Sal"]))
print()
conn.close()
