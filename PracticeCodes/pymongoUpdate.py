#Update pymongo
from pymongo import MongoClient
conn=MongoClient("localhost",27017)
# 2 Access The database
db=conn.test9.Empl

oldEname = input("Enter the Ename to update")

myquery = { "Ename":oldEname }

newEname = input("Enter new Ename")
newvalues = { "$set": { "Ename":newEname } }

db.update_one(myquery, newvalues)

#Display Values:
for x in db.find():
  print(x) 
