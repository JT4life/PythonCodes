#Insert collection pymongo
from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Empl

try:
    document = []
    document.append({
        'Empno':5,
        'Ename':'J',
        'Sal':66
        })
    document.append({
        'Empno':6,
        'Ename':'B',
        'Sal':88
        })
    document.append({
        'Empno':7,
        'Ename':'M',
        'Sal':55
        })

    db.insert_many(document)

except:
    print("error")

#Display Values:
for x in db.find():
  print(x) 
